# Install library directly from GitHub
devtools::install_github("AlbertRapp/tidychatmodels")
library(tidychatmodels)
library(dplyr)

# API Key Setup
chat_ollama <- create_chat('ollama') 
chat_ollama

# Make a virtual chatbot that is designed to return R code
rcode_chatbot <- chat_ollama %>%
  add_model("gemma:7b") %>%
  add_params("temperature"=0, "max_tokens"=2500) %>%
  add_message(
    role="system",
    message="You are a chatbot that writes R programs and R code scripts.
    You only return R code. Do not return anything else."
  )

# Ask an R code question
rcode_chatbot_message_added <- rcode_chatbot %>%
  add_message(
    role="user",
    message="Create a shiny app that includes a dataset such as
    mtcars and makes a visualization using plotty for columns that the user selects.
    Allow the user to upload an Excel file or CSV file that changes the data being analyzed by
    the plotly plot"
  )

# Perform the chat
rcode_chatbot_result <- rcode_chatbot_message_added %>% perform_chat()

# Extract results as a dataframe
rcode_chatbot_result %>% extract_chat(silent = TRUE)
rcode_chatbot_result %>%
  extract_chat(silent = TRUE) %>%
  pluck("message", 3) %>%
  cat()

