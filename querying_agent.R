library(httr)

# Querying Agent function to send a query to Laptop 2
querying_agent <- function(query) {
  # Replace <Laptop_2_IP> with the actual IP address of Laptop 2
  url <- paste0("http://127.0.0.1:3836/respond?query=", URLencode(query))
  response <- GET(url)
  
  # Check if the response was successful
  if (status_code(response) != 200) {
    stop(paste("Error:", status_code(response), ":", http_status(response)))
  }
  
  # Parse the response as JSON
  content <- content(response, "parsed")
  
  # Output the response from Laptop 2
  print(content$response[[1]])
  return(content$response[[1]])
}

# Example query
response <- querying_agent("What is your name?")
