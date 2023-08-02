# **Detección y rastreo de perfiles con posibles tendencias suicidas en blogs y redes sociales**

Este repositorio corresponde al trabajo realizado por Orlando Alvarez [(ver contribuidores)](#contribuidores) para el Segundo Verano Nacional de Investigación en Ciencia y Tecnología del TecnNM 2023.

## **Sobre el proyecto**

> A grosso modo, el proyecto consiste en reunir información de blogs y redes sociales, para posteriormente procesarla y crear un repositorio de datos que permita a especialistas detectar perfiles con posibles tendencias suicidas.

<details> <summary>✨ Haz click en esta lista desplegable para ver los objetivos ✨</summary>
<h2><b>🎯 Objetivo general</b></h2>
Por medio del uso de herramientas tecnológicas y con la ayuda de redes sociales y medios de comunicación digitales, identificar perfiles de usuarios suicidas o posibles usuarios en riesgo de suicidio.

<h2><b>♦ Objetivos específicos</b></h2>
Recopilar y guardar comentarios o publicaciones de redes sociales como>
<ul>
<li>🦜 Twitter</li>
<li>📘 Facebook</li>
<li>📷 Instagram</li>
<li>🎵 TikTok</li>
<li>▶ YouTube</li>
</ul>
... así como foros, blogs y comentarios de otras plataformas, relacionadas con las siguientes temáticas:</li>
<ul>
<li>Comportamiento impulsivo</li>
<li>Duelo o perdida de seres queridos (Familia, amigos, mascotas)</li>
<li>Problemas de relaciones maritales/amorosos</li>
<li>Conflictos parentales o violencia intrafamiliar</li>
<li>Acoso escolar</li>
<li>Trastornos médicos dolorosos</li>
<li>Enfermedades mentales</li>
<li>Sentimientos de tristeza o desesperanza</li>
<li>Estrés financiero (Problemas monetarios, deudas o desempleo)</li>
<li>Experiencias traumáticas (Abuso físico o sexual)</li>
<li>Periodos de transición (Jubilaciones, retiros)</li>
<li>Expresiones de ansiedad o signos de angustia</li>
<li>Depresión</li>
<li>Menciones de pensamientos suicidas (Bromas o chistes incluidos)</li>
</ul>
</details>

<br>

## **Mi contribución**

> _Dado un conjunto de datos de Twitter:_
>    1. Crear una lista negra de usuarios que hagan spam, se dediquen a publicar noticias, o que difundan la importancia de la salud mental.
>    2. Dada dicha lista, retirar a esos ususarios del conjunto de datos.

🌐 Además, contribuí a la revisión de los scripts de web scrapping que se encuentran en el repositorio, así como procesé los resultados de esta actividad para conseguir conjuntos de datos limpios y semejantes a los provistos.

📄 Por su parte, realicé scripts de [instalación de dependencias y configuración de variables de entorno](#para-ejecutarcontribuir) para facilitar la ejecución de los notebooks de este repositorio, con ayuda de GitHub Copilot 🤖.

## **Contenido**
En este repositorio, se destacan los siguientes archivos:

1. Emplea web scrapping para extraer información de blogs y redes sociales.

implementan diferentes técnicas de procesamiento de lenguaje natural para la detección y rastreo de perfiles con posibles tendencias suicidas en blogs y redes sociales.

* **Cuaderno [`lista_negra`](./lista_negra.ipynb)**
    * En él, se procesan publicaciones extraídas de Twitter, que contienen palabras clave relacionadas con las temáticas enlistadas previamente, tales como "ahorcarme" o "quiero morir".
    * El objetivo de este cuaderno es filtrar los usuarios que publican más de `n` veces para hacer una revisión manual de los tweets y, una vez que se encuentren palabras/frases comunes entre los usuarios cuyo contenido es considerado despreciable (como la palabra "colgar", refiriéndose a una llamada telefónica, o la publicación repetitiva de letras de canciones), se puedan aplicar funciones que detecten esos patrones de manera automática y recopilen a los usuarios que los presenten, a fin de aminorar la cantidad de publicaciones que puedan encontrarse que no sean de interés, y, en futuras iteraciones, excluir a estos usuarios al realizar llamadas a la API de Twitter.
* **Cuaderno [`filtrado_publicaciones_por_contexto`](./filtrado_publicaciones_por_contexto.ipynb)**
    * Aquí lleva a profundidad el objetivo del cuaderno anterior y emplea los servicios de Azure (y de su integración con OpenAI) para continuar clasificando las frases que contienen la palabra "colgarme" y hacen uso de ella refiriéndose a colgarse algo, o a depender/aprovecharse de alguien. De la misma manera, es posible detectar el uso descontextualizado de otras palabras o frases.
        * Si bien la clasificación de textos de manera automatizada puede no otorgar resultados precisos, es posible jugar con las solicitudes que se hacen al modelo de lenguaje para que este ofrezca un punto de partida en la clasificación o limpieza de textos.
        * Si deseas ejecutar este cuaderno, es necesario que cuentes con una cuenta de Azure y que tengas acceso a los servicios de Azure OpenAI. Para más información, consulta la [documentación oficial](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/).
* **Cuaderno [`preprocesamiento_hilos_4chan`](./preprocesamiento_hilos_4chan.ipynb)**
    * En este archivo se trabaja sobre una serie conjuntos de datos que reúnen publicaciones de hilos populares de la red social 4chan, mismos que son característicos por su tono hostil y de burla. Aprovechándonos de una [serie de artículos](#Referencias) que contienen palabras o frases típicamente empleadas por personas con tendencias suicidas, se filtran los hilos que contienen dichas palabras o frases.
    * Esta fuente de información es beneficiosa, debido a que los posts de estos usuarios están en inglés, con lo que favorecemos la generalización de los modelos que puedan construirse con esta información.
* **Script [`prereq.ps1`](./prereq.ps1)**
    * Este script de PowerShell instala las dependencias necesarias para ejecutar los cuadernos de este repositorio. Para ejecutarlo, es necesario una instalación de Python 3 y R.
* **Script [`tumblr_scrapper_script.ps1`](./tumblr_scrapper_script.ps1)**
    * Este script de PowerShell ejecuta el script de Python que se encuentra en la carpeta [Scraper-Tumblr](./Tumblr_Scrapper/tumblr_scrapper/tumblr_scrapper/) de manera automatizada para una serie de blogs especificados, mismos que se encuentran en la definición del script. 

## **Para ejecutar/contribuir**

🐍 Antes que nada, asegúrate de tener una instalación de Python 3 y R. ®

Si deseas ejecutar o contribuir a uno de los notebooks de este repositorio, por favor, corre el script de prerrequisitos:

```powershell
.\prereq.ps1
```

Este script instalará las dependencias necesarias para ejecutar los cuadernos de este repositorio. Aquellas dependencias correspondientes a Python, se instalarán en un entorno virtual llamado `venv-tendencias` en la carpeta raíz del repositorio.

### Para usar el cuaderno `filtrado_publicaciones_por_contexto.ipynb`

Edita el archivo `.env` (este se crea después de instalar los prerrequesitos) y agrega las credenciales de Azure OpenAI; el archivo deberá verse de la siguiente manera:

```
OPENAI_API_KEY=escribe_tu_llave_aqui
OPENAI_ENDPOINT=url_de_tu_modelo
``` 

**Nota:** asegúrate de tener un deployment del modelo `gpt-35-turbo` en tu cuenta de Azure OpenAI.

## **Contribuidores**
#### 👨‍💻 [Miguel Fernández](https://github.com/Maxrealms2002)

* Scripts de Python para scrapping de [4chan](./Scraper-4chan/v2/README.txt) y [Tumblr (ir a repositorio original)](https://github.com/Maxrealms2002/Tumblr_Scrapper).

## **Referencias**
> Borghero, F.; Quiroz D.; et. al. (Septiembre 2014). Guía para pacientes y familiares. _Conociendo el Trastorno Bipolar_. Ministerio de Salud, Sociedad Chilena de Trastornos Bipolares. Santiago.

> Luo J, Du J, Tao C, Xu H, Zhang Y. _Exploring temporal suicidal behavior patterns on social media: Insight from Twitter analytics_. Health Informatics Journal. 2020;26(2):738-752. doi:10.1177/1460458219832043
    
