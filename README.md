# Detección y rastreo de perfiles con posibles tendencias suicidas en blogs y redes sociales

Este repositorio contiene múltiples scripts y/o programas en los que se implementan diferentes técnicas de procesamiento de lenguaje natural para la detección y rastreo de perfiles con posibles tendencias suicidas en blogs y redes sociales.

* En el cuaderno [lista_negra](./lista_negra.ipynb) se procesan publicaciones extraídas de Twitter, que contiene las palabras "ahorcarme" y "colgarme". El propósito del código que contienen es revisar publicaciones que puedan ser spam, o que empleen dichas palabras en un contexto diferente al de una tendencia suicida (como la palabra "colgar", refiriéndose a una llamada telefónica). 
    * Una vez que se obtienen esos usuarios con múltiples publicaciones y que usan las palabras fuera del contexto de interés, se revisan manualmente para descartar, además, perfiles que publiquen noticias.
* El archivo [filtrado_publicaciones_por_contexto](./filtrado_publicaciones_por_contexto.ipynb) lleva a profundidad el objetivo del cuaderno anterior y emplea los servicios de Azure (y de su integración con OpenAI) para continuar clasificando las frases que contienen la palabra "colgarme" y hacen uso de ella refiriéndose a colgarse algo, o a depender/aprovecharse de alguien. De la misma manera, es posible detectar el uso descontextualizado de otras palabras o frases.
    * La revisión de cada post no debe ser tan exhaustiva, pues ser muy rigurosos podría hacernos perder información importante, y aunque buscamos reducir la cantidad de falsos positivos, el objetivo principal es tener una alta sensibilidad (pocos falsos negativos).
    * Si deseas ejecutar este cuaderno, es necesario que cuentes con una cuenta de Azure y que tengas acceso a los servicios de Azure OpenAI. Para más información, consulta la [documentación oficial](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/).
* En el notebook [filtrado_hilos_4chan](./filtrado_hilos_4chan.ipynb) se trabaja sobre una serie de hilos populares de la red social 4chan, mismos que son característicos por su tono hostil y de burla. Aprovechándonos de una [serie de artículos](#Referencias) que contienen palabras o frases típicamente empleadas por personas con tendencias suicidas, se filtran los hilos que contienen dichas palabras o frases.
    * Esta fuente de información es beneficiosa, debido a que los posts de estos usuarios están en inglés, con lo que favorecemos la generalización de los modelos que se construyan.

## Para ejecutar/contribuir

Si deseas ejecutar o contribuir a uno de los notebooks de este repositorio, por favor, corre el script de prerrequisitos:

```powershell
.\prereq.ps1
```

Posteriormente, edita el archivo `.env` y agrega las credenciales de Azure OpenAI.

El archivo deberá verse de la siguiente manera:

```
OPENAI_API_KEY=escribe_tu_llave_aqui
OPENAI_ENDPOINT=url_de_tu_modelo
``` 

**Nota:** asegúrate de tener un deployment del modelo `gpt-35-turbo` en tu cuenta de Azure OpenAI.

## Referencias
<blockquote>
    Borghero, F.; Quiroz D.; et. al. (Septiembre 2014). Guía para pacientes y familiares. _Conociendo el Trastorno Bipolar_. Ministerio de Salud, Sociedad Chilena de Trastornos Bipolares. Santiago.
</blockquote>
    