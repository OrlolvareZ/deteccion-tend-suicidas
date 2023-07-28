# Corrige el charset a UTF-8
chcp 65001

# Revisa si las variables de entorno están definidas
if ($env:TUMBLR_EMAIL -eq $null -or $env:TUMBLR_PASSWORD -eq $null) {
    Write-Host "Por favor especifica tu correo y contrasena de Tumblr:"
    Write-Host "Correo: "
    $env:TUMBLR_EMAIL = Read-Host
    Write-Host "Contrasena: "
    # Oculta la contraseña
    $env:TUMBLR_PASSWORD = Read-Host -AsSecureString

    # Guarda las variables de entorno
    [Environment]::SetEnvironmentVariable("TUMBLR_EMAIL", $env:TUMBLR_EMAIL, "User")
    [Environment]::SetEnvironmentVariable("TUMBLR_PASSWORD", $env:TUMBLR_PASSWORD, "User")
}

Set-Location "./Tumblr_Scrapper/tumblr_scrapper/tumblr_scrapper" # Ubicación del scrapper

Write-Host "Comenzando el scrapper de Tumblr..."
Write-Host "¿Cuantas iteraciones en cada blog quieres realizar?"
$iterations = Read-Host

$DEF_FOLDER = "./datasets"

# Lista de blogs a scrapear
$blogs = @(
    "crowsareverytired",
    "icecold-snow-angel2",
    "share-a-coke-with-ana",
    "hearttattack",
    "caffeinatedopossum",
    "urlocalmentallyunstablegal",
    "plutobbyyy",
    "sad-boi-shit",
    "sk1nnyan93l",
    "dizzyoffpassion",
    "black-coffee-and-boness",
    "problematicpastries",
    "organicclown",
    "cemeteryrocks900",
    "luxsmall",
    "pinecalz"
)

# Ejecuta el scrapper por cada blog

for ($i = 0; $i -lt $blogs.Count; $i++) {
    $blog = $blogs[$i]
    $url = "https://www.tumblr.com/$blog"
    $output_file = "$DEF_FOLDER/$blog.csv"
    scrapy crawl tumblr -a email="$env:TUMBLR_EMAIL" -a password="$env:TUMBLR_PASSWORD" -a url="$url" -a iterations=$iterations -o $output_file
}
