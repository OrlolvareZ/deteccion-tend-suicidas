# Script de web scrapping que usa Scrapy y Selenium para obtener nombres de usuarios
# texto de los post principales y su correspondiente url de un blog de tumblr.

import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from ..items import TumblrScrapperItem


class TumblrSpider(scrapy.Spider):
    # Nombre de la araña para ejecutar el script
    name = "tumblr"
    comment_url = []  # Lista para almacenar las URLs de los comentarios

    # Funcion que nos permite introducir los siguientes parametros:
        # email: Es el correo electronico asociado a nuestra cuenta de tumblr
        # password: Es la contraseña asociada al correo de nuestra cuenta de tumblr
        # url: Es la url del blog de tumblr que se desea scrapear
        # iterations: Es la cantidad de contenido que cargara por cada scroll down para Scrapear (Tumblr carga contenido de forma dinamica, para ello hay que hacer scroll down a atraves del blog)

    def __init__(self, email=None, password=None, url=None, iterations=1, *args, **kwargs):
        super(TumblrSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]
        self.iterations = int(iterations)
        self.email = str(email)
        self.password = str(password)

    # Funcion que ejecuta el codigo principal

    def parse(self, response):
        #Obtenemos la URL de la pagina que introdujo el usuario
        current_url = response.url
        # Abrimos el navegador en la pagina de login de tumblr
        driver = webdriver.Chrome()
        driver.get('https://www.tumblr.com/login')

        # Realizamos el inicio de sesion en tumblr
        # Encuentra los campos de entrada de correo electrónico y contraseña y envía las credenciales.
        email_input = driver.find_element(By.NAME, 'email')
        email_input.send_keys(self.email)

        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        # Espera unos segundos para que se complete el inicio de sesión.
        time.sleep(1)

        # Nos redirige a la url del blog de tumblr
        driver.get(current_url)
        time.sleep(2)

        # Hacemos 'n' scrolldown dentro del blog para cargar contenido 
        for i in range(self.iterations):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # Esperar unos segundos para que la página cargue los nuevos elementos
            time.sleep(4)
        
        # Regresamos hasta al inicio de la pagina del blog
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

        # Realizamos el procedimiento para hacer click en todos los botones de la pagina 
        # con el fin de obtener todos los links de cada post
        try:
            buttons = driver.find_elements(By.CSS_SELECTOR, '.a_qtV .EvhBA') # Obtiene todos los botones del blog

            # Bucle que prescionara y recopilara cada url de cada post
            for button in buttons:
                # Hacemos un primer click en el boton para cargar el contenido dinamico de la url
                button.click()
                
                #Obtenemos la url y la añadimos a nuestra lista de urls
                elemento_link = driver.find_element(By.CSS_SELECTOR, 'a.X1uIE.XOf8k.qYCWv.v_1X3')
                url = elemento_link.get_attribute('href')
                TumblrSpider.comment_url.append(url)

                # Volvemos a prescionar el boton para evitar tapar con el contenido el siguiente elemento boton.
                # Ademas esperamos un poco de tiempo para evitar prescionar otro campo accidentalmente
                button.click()
                time.sleep(0.5)
        except:
            print("Error al hacer clic en el botón:")

        time.sleep(2)

        # Guardamos el codigo fuente de la pagina con todo el nuevo contenido cargado dinamicamente
        page_source = driver.page_source

        # Cerramos el navegador
        driver.quit()

        # Continuamos con el analisis de la pagina utilizando Scrapy
        articles = scrapy.Selector(text=page_source).css('.ge_yK > .c79Av > .r0etU')
        for i, article in enumerate(articles):
            # Obtenemos el nombre de usuario
            user_names = article.css('.sqHC2 , .NStl8 .BSUG4').css('::text').extract()
            # Utilizamos extract() para obtener ambos párrafos
            user_comments = []
            comment_sections = article.css('.GzjsW')

            # Dentro de cada sección de comentarios, podemos encontrar rupturas en la continuidad del texto,
            # debido a la presencia de enlaces. Estos abren una etiqueta aparte y agregan más elementos a la lista
            # de lo que hay usuarios en el artículo. Por lo tanto, en vez de usar extract() para obtener el texto
            # en todas las secciones a la vez, lo usamos por sección.
            for section in comment_sections:
                comment = ' '.join(section.css('::text').extract())
                user_comments.append(comment)
            
            # Tras bambalinas, Scrapy colocará los comentarios y los nombres de usuario en un objeto de tipo lista,
            # pues típicamente se encontrará más de uno por cada post.
            for user_name, user_comment in zip(user_names, user_comments): # Iteramos sobre los comentarios y nombres de usuario a la vez
                
                # Eliminamos los saltos de linea y espacios en blanco de los comentarios
                user_comment = user_comment.replace('\n', '. ').strip()
                
                # Almacenamos el contenido scrapeado en contenedores para guardarlos como archivos JSON/CSV
                items = TumblrScrapperItem(
                    user_name=user_name,
                    user_comment=user_comment,
                    comment_url=TumblrSpider.comment_url[i]
                )
                yield items
