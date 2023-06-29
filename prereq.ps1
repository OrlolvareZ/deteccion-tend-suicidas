# Preconfiguración de entorno de desarrollo (Python)

# Creación de entorno virtual
python -m venv .\venv-tendencias
.\venv-tendencias\Scripts\Activate.ps1

# Herramientas para el cuaderno de filtrado de publicaciones de acuerdo al contexto
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
New-Item -ItemType File -Name ".env"

# Herramienta para mejorar la fusión de cambios de los notebooks
pip install nbdev
nbdev_install_hooks