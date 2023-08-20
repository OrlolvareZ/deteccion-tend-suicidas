# WEB SCRAPPING 4CHAN v1

Primera versión del Web Scraper para 4Chan. Más específicamente, busca en el catálogo de un foro dado en 4Chan todos los comentarios, archivos y metadatos asociados con la ayuda de la Biblioteca Python BASC 4Chan.

---

## Requerimientos

1. Instalar las siguientes librerías:
   - **BASC_py4chan==0.6.5**
   - **tqdm==4.46.1**

2. Si tienes una versión de Python 3.9 o superior, debes reemplazar el código en el archivo `util.py` en la siguiente ruta:

    ```
    c:\users\[Nombre de usuario]\appData\local\programs\python\python[versión]\lib\site-packages\basc_py4chan\util.py
    ```

    **Ejemplo:**

    ```
    C:\Users\migue\AppData\Local\Programs\Python\Python310\Lib\site-packages\basc_py4chan\util.py
    ```

    El archivo a reemplazar se encuentra en el repositorio.

    Contenido del archivo `util.py` a reemplazar:

    ```python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    """Funciones de utilidad."""

    import re
    import sys

    # Corrección de compatibilidad del analizador HTML para Python 3.9 en adelante
    if sys.version_info[0] == 3 and sys.version_info[1] >= 9:
        import html
        _parser = html
    else:
        # El analizador HTML cambió de nombre en Python 3.x
        try:
            from html.parser import HTMLParser
        except ImportError:
            from HTMLParser import HTMLParser

        _parser = HTMLParser()

    def clean_comment_body(body):
        """Devuelve el HTML del comentario dado como texto plano.

        Convierte todas las etiquetas y entidades HTML dentro de los comentarios de 4chan
        en equivalentes de texto legibles por humanos.
        """
        body = _parser.unescape(body)
        body = re.sub(r'<a [^>]+>(.+?)</a>', r'\1', body)
        body = body.replace('<br>', '\n')
        body = re.sub(r'<.+?>', '', body)
        return body
    ```

---

## Ejecución

Se ejecuta desde la terminal y el programa acepta los siguientes parámetros:

1. **--board_name**
   - Tablero de 4Chan en el cual se recopilará la información (Obligatorio)
2. **--num_threads**
   - Número de hilos en los que se recopilará información (Obligatorio)
3. **--debug**
   - Información adicional (Opcional)

**Ejemplo de ejecución:**

```bash
python 4chan_scraper.py --board_name "pol" --num_threads 5 --debug "False"