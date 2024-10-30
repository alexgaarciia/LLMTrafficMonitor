# Install necessary packages if not already installed
if (!requireNamespace("plumber", quietly = TRUE)) install.packages("plumber")
if (!requireNamespace("httr", quietly = TRUE)) install.packages("httr")

# Load the required libraries
library(plumber)
library(httr)

# Define the response function
#* @param query The query to respond to
#* @get /respond
function(query = "") {
  # Define the API URL
  url <- "http://localhost:1234/v1/chat/completions"
  
  # Prepare the request body as a JSON list
  body <- list(
    model = "lmstudio-community/gemma-2-9b-it-GGUF",
    messages = list(
      list(role = "system", content = "You are the responding agent. Answer the query."),
      list(role = "user", content = query)
    ),
    temperature = 0.7,
    max_tokens = 250,
    stream = FALSE
  )
  
  # Make the POST request to LM Studio API
  response <- POST(url, 
                   add_headers(`Content-Type` = "application/json"), 
                   body = body, 
                   encode = "json")
  
  # Process the response
  if (status_code(response) == 200) {
    # Extract the content of the response
    result <- content(response, as = "parsed", type = "application/json")
    reply <- result$choices[[1]]$message$content
    list(response = reply)
  } else {
    # If there's an error, return the error message
    list(error = paste("Error:", status_code(response)), 
         details = content(response, as = "text"))
  }
}

# To run the API, save this script and run it as follows:
# plumb(file='responding_agent_LM_Studio.R')$run(port=3836)
