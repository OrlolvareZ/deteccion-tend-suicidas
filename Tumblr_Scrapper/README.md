# Tumblr_Scrapper

Este es un script de web scraping que utiliza Scrapy y Selenium para obtener nombres de usuarios, texto de los posts principales y sus correspondientes URLs de un blog de Tumblr.

## Instalación

1. Descarga (clona) el archivo del repositorio de GitHub.

2. Crea un entorno virtual y actívalo.

3. Instala los paquetes del archivo `requirements.txt` usando el siguiente comando:

```
	pip install -r requirements.txt
```

4. Ve a la carpeta `tumblr_scrapper` que contiene el spider de Scrapy:

```
 	cd tumblr_scrapper/tumblr_scrapper
```

5. Actualiza el driver de Chrome de acuerdo a tu version del navegador:

 - Para ello deberas ir al siguiente sitio web y descargar la version que coincida o que más se aproxime al tuyo:
   
   - `https://googlechromelabs.github.io/chrome-for-testing/` Si tu version de Google Chrome es mayor o igual a 115
   - `https://chromedriver.chromium.org/downloads` Si tu version de Google Chrome es anterior a 115
     
 - Ahora en la carpeta `spider`, remplaza el archivo `chromedriver.exe` con el que acabas de descargar.
   	
6. Para ejecutar el script, necesitas introducir un comando en la terminal de la siguiente manera:

```
	scrapy crawl tumblr -a email="email" -a password="password" -a url='url' -a iterations=n -o output_name.jsonl
```

Donde:

- `email`: Es el correo electrónico asociado a nuestra cuenta de Tumblr.
- `password`: Es la contraseña asociada al correo de nuestra cuenta de Tumblr.
- `url`: Es la URL del blog de Tumblr que se desea scrapear.
- `iterations`: Es la cantidad de contenido que se cargará por cada scroll down para el scraping (Tumblr carga contenido de forma dinámica, por lo que hay que hacer scroll down a través del blog).
- `output_name`: Nombre del archivo JSONL o CSV que contendrá los datos scraped.

## Consideraciones

- La velocidad de este web scraping dependerá de cuántas iteraciones se utilicen. Por lo general, 30 iteraciones tardarán aproximadamente 20 minutos. Esto se debe al uso de Selenium debido a la naturaleza dinámica de la página, que solo carga los enlaces de las publicaciones cuando interactúas con los botones.

- No es posible scrapear todo tipo de blog de Tumblr, solo funciona con blogs de estilo estándar. Una buena forma de diferenciarlo es basándose en el URL, como se muestra a continuación:

- `https://www.tumblr.com/hearttattack` (Página estándar - SÍ se puede scrapear)
- `https://sleep-sounds-nice-rn.tumblr.com` (Página personalizada - NO se puede scrapear)

- En caso de ya tener instalado la libreria de `Selenium` en tu equipo con anterioridad. Dirigete a una ruta similar a esta en tu equipo y remplaza el archivo descargado en la carpeta de la version de tu driver actual:

```
	C:\Users\[User_name]\.cache\selenium\chromedriver\win32
```	
