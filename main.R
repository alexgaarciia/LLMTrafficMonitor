# Install library directly from GitHub
devtools::install_github("AlbertRapp/tidychatmodels")
library(tidychatmodels)

# API Key Setup
usethis::edit_r_environ()
my_api_key <- Sys.getenv('lm-studio')
