# Detección y rastreo de perfiles con posibles tendencias suicidas en blogs y redes sociales

Este repositorio contiene múltiples scripts y/o programas en los que se implementan diferentes técnicas de procesamiento de lenguaje natural para la detección y rastreo de perfiles con posibles tendencias suicidas en blogs y redes sociales.

* En el cuaderno [lista_negra](./lista_negra.ipynb) se procesan publicaciones extraídas de Twitter, que contiene las palabras "ahorcarme" y "colgarme". El propósito del código que contienen es revisar publicaciones que puedan ser spam, o que empleen dichas palabras en un contexto diferente al de una tendencia suicida (como la palabra "colgar", refiriéndose a una llamada telefónica). 
    * Una vez que se obtienen esos usuarios con múltiples publicaciones y que usan las palabras fuera del contexto de interés, se revisan manualmente para descartar, además, perfiles que publiquen noticias.
* El archivo [filtrado_tweets_ahorcarme](./filtrado_tweets_ahorcarme.ipynb) lleva a profundidad el objetivo del cuaderno anterior y emplea los servicios de Azure (y de su integración con OpenAI) para continuar clasificando las frases que contienen la palabra "ahorcarme" y hacen uso de ella refiriéndose a colgarse algo, o a depender/aprovecharse de alguien.
* En el notebook [filtrado_hilos_4chan](./filtrado_hilos_4chan.ipynb) se trabaja sobre una serie de hilos populares de la red social 4chan, mismos que son característicos por su tono hostil y de burla. Aprovechándonos de una [serie de artículos](#Referencias) que contienen palabras o frases típicamente empleadas por personas con tendencias suicidas, se filtran los hilos que contienen dichas palabras o frases.
    * Esta fuente de información es beneficiosa, debido a que los posts de estos usuarios están en inglés, con lo que favorecemos la generalización de los modelos que se construyan.
## Para contribuir

Si deseas contribuir a uno de los notebooks de este repositorio, por favor, corre el script de prerrequisitos:

```powershell
.\prereq.ps1
```

## Referencias
    