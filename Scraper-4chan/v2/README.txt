============================
|| WEB SCRAPPING 4CHAN v1 ||
============================

Primera version del Web Scrapper para 4Chan. Mas especificamente, busca en el catálogo de un foro dado en 4Chan todos los comentarios, archivos y metadatos asociados con la ayuda de BASC 4Chan Python Library.

--------------------------------------------
========== ***REQUERIMIENTOS*** ========== 
--------------------------------------------
1) Instalar las siguientes librerias:
** BASC_py4chan==0.6.5
** tqdm==4.46.1

2) Si se tiene una version de python 3.9 o superior, entonces se tiene que remplazar el codigo de util.py en la siguiente ruta:

c:\users\[Nombre de usuario]\appData\local\programs\python\python[version]\lib\site-packages\basc_py4chan\util.py

>>> Ejemplo <<<
C:\Users\migue\AppData\Local\Programs\Python\Python310\Lib\site-packages\basc_py4chan\util.py

El archivo se deja en el repositorio:

>>> CODIGO util.py a remplazar <<<
_____________________________________________________________
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utility functions."""

import re
import sys

#HTML parser compat fix for python 3.9 and onwards
if sys.version_info[0] == 3 and sys.version_info[1] >= 9:
    import html
    _parser = html 
else:
    # HTML parser was renamed in python 3.x
    try:
        from html.parser import HTMLParser
    except ImportError:
        from HTMLParser import HTMLParser

    _parser = HTMLParser()

def clean_comment_body(body):
    """Returns given comment HTML as plaintext.

    Converts all HTML tags and entities within 4chan comments
    into human-readable text equivalents.
    """
    body = _parser.unescape(body)
    body = re.sub(r'<a [^>]+>(.+?)</a>', r'\1', body)
    body = body.replace('<br>', '\n')
    body = re.sub(r'<.+?>', '', body)
    return body
___________________________________________________________

--------------------------------------------
========== ***EJECUCION*** ========== 
--------------------------------------------
> Se ejecuta desde la terminal y el programa tiene los siguientes parametros:

1. **--board_name**
   - Tablero de 4Chan en el cual se recopilara la informacion (Obligatorio)
2. **--num_threads**: 
   - Numero de hilos en los que se recopilara informacion (Obligatorio)
3. **--debug**:
   - Informacion adicional (Opcional)

>>> Ejemplo <<<
python 4chan_scraper.py --board_name "pol" --num_threads 5 --debug "False"