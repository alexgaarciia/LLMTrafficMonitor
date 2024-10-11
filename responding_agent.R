# responding_agent_v2.R

library(plumber)
library(tidychatmodels)

# Function for responding to queries from Laptop 1
#* @param query The query to respond to
#* @get /respond
function(query="") {
  chat_ollama <- create_chat('ollama') %>%
    add_model("gemma:7b") %>%
    add_params("temperature"=0.7, "max_tokens"=2500) %>%
    add_message(
      role = "system",
      message = "You are the responding agent. You reply to queries from the querying agent."
    ) %>%
    add_message(role = "user", message = query)
  
  response <- chat_ollama %>%
    perform_chat() %>%
    extract_chat()
  
  list(response = response$message[[3]])
}
