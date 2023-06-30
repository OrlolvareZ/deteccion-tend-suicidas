install.packages(
    c(
        "tm",
        "SnowballC",
        "dplyr",
        "rjson",
        "stringr",
        "IRkernel",
        "languageserver",
    ),
    repos = "http://cran.us.r-project.org",
)

IRkernel::installspec()
