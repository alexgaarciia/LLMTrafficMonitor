# Install httr if not already installed
if (!requireNamespace("httr", quietly = TRUE)) install.packages("httr")

# Load the httr package
library(httr)

# Define the API URL
url <- "http://localhost:1234/v1/chat/completions"

# Define the request body as a JSON string
body <- list(
  model = "llama-2-13b-chat",
  messages = list(
    list(role = "system", content = "Always answer in rhymes. Today is Thursday"),
    list(role = "user", content = "What day is it today?")
  ),
  temperature = 0.7,
  max_tokens = -1,
  stream = FALSE
)

# Make the POST request
response <- POST(url, 
                 add_headers(`Content-Type` = "application/json"), 
                 body = body, 
                 encode = "json")

# Check the response status and parse the JSON content
if (status_code(response) == 200) {
  result <- content(response, as = "parsed", type = "application/json")
  print(result$choices[[1]]$message$content)
} else {
  print(paste("Error:", status_code(response)))
  print(content(response, as = "text"))
}
