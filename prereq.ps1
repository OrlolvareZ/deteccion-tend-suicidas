function refresh-path {
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") +
                ";" +
                [System.Environment]::GetEnvironmentVariable("Path","User")
}

# Preconfiguración de entorno de desarrollo

# Revisar instalación de Python y pip

$PythonPath = Get-Command python -ErrorAction SilentlyContinue
$PipPath = Get-Command pip -ErrorAction SilentlyContinue

if (-not $PythonPath -or -not $PipPath) {

    Write-Host "Python and/or pip are not installed. Please install Python and the pip package manager."
    Write-Host "Install pip with the command: python -m ensurepip --upgrade"
    exit
}

# Crear entorno virtual

python -m venv .\venv-tendencias
.\venv-tendencias\Scripts\Activate.ps1

# Herramientas para python y jupyter
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
New-Item -ItemType File -Name ".env"


# Obtener la ruta de instalación de R

# Probar si R está en la variable de entorno PATH
$RPath = Get-Command Rscript -ErrorAction SilentlyContinue

if (-not $RPath) {
    Write-Host "Locating R installation..."
    $RPath = Get-ChildItem -Path "C:\" -Filter "R.exe" -Recurse -ErrorAction SilentlyContinue

    if (-not $RPath) {
        Write-Host "R installation not found. Please download and install R from https://cran.r-project.org/"
        exit
    }

    # Añadir la ruta de instalación de R al PATH
    $RPath = $RPath[1].Directory.FullName
    [System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";$RPath", "Machine")

    refresh-path
    Write-Host "Added R installation to PATH."
}

# Herramientas para R, leer el archivo "requirements.R"

Rscript requirements.R

# Herramienta para mejorar la fusión de cambios de los notebooks
pip install nbdev
nbdev_install_hooks