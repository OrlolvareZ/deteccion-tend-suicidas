# Preconfiguración de entorno de desarrollo (Python)

# Creación de entorno virtual
python -m venv .\venv-tendencias
.\venv-tendencias\Scripts\Activate.ps1

# Herramientas para python y jupyter
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
New-Item -ItemType File -Name ".env"

# Herramientas para R, leer el archivo "requirements.R"

Rscript requirements.R

# Herramienta para mejorar la fusión de cambios de los notebooks
pip install nbdev
nbdev_install_hooks