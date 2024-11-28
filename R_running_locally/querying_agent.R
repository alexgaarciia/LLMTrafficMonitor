library(httr)

# Querying Agent function to send a query to Laptop 2
querying_agent <- function() {
  repeat {
    # Prompt the user to input a query
    query <- readline(prompt = "Enter your query (type 'exit' to stop): ")
    
    # Check if the user wants to stop
    if (tolower(query) == "exit") {
      cat("Exiting the querying agent.\n")
      break
    }
    
    # Replace <Laptop_2_IP> with the actual IP address of Laptop 2
    url <- paste0("http://127.0.0.1:3836/respond?query=", URLencode(query))
    response <- GET(url)
    
    # Check if the response was successful
    if (status_code(response) != 200) {
      cat(paste("Error:", status_code(response), ":", http_status(response)), "\n")
      next  # Skip this iteration and ask for another query
    }
    
    # Parse the response as JSON
    content <- content(response, "parsed")
    
    # Output the response from Laptop 2
    print(content$response[[1]])
  }
}

querying_agent()
