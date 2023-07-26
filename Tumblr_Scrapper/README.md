# Tumblr_Scrapper

Este es un script de web scraping que utiliza Scrapy y Selenium para obtener nombres de usuarios, texto de los posts principales y sus correspondientes URLs de un blog de Tumblr.

## Instalación

1. Descarga (clona) el archivo del repositorio de GitHub.

2. Crea un entorno virtual y actívalo.

3. Instala los paquetes del archivo `requirements.txt` usando el siguiente comando:

	pip install -r requirements.txt

4. Ve a la carpeta `tumblr_scrapper` que contiene el spider de Scrapy:

 	cd tumblr_scrapper/tumblr_scrapper

5. Para ejecutar el script, necesitas introducir un comando en la terminal de la siguiente manera:

	scrapy crawl tumblr -a email="email" -a password= -a url='url' -a iterations=n -o output_name.jsonl

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

Al seguir estas instrucciones, podrás utilizar el script para obtener datos de un blog de Tumblr específico. Recuerda siempre tener en cuenta las consideraciones mencionadas y respetar los términos de uso de la plataforma al realizar scraping de datos.
