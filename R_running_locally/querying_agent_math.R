library(jsonlite)
library(httr)

################################################################################
# Extract questions from the JSON file
################################################################################

# Read the JSONL file line by line and extract the 'question' field
file_path <- "../data/test.jsonl"
questions <- c()

# Open the file and read each line
test_data <- file(file_path, "r")
while (TRUE) {
  line <- readLines(test_data, n = 1, warn = FALSE)
  if (length(line) == 0) break  # Stop if end of file
  
  # Parse the JSON line and extract the question
  json_data <- fromJSON(line)
  questions <- c(questions, json_data$question)
}
close(test_data)



################################################################################
# Definition of querying agent
################################################################################

# Querying Agent function to send a query to Laptop 2
querying_agent <- function(questions) {
  for (query in questions) {
    url <- paste0("http://127.0.0.1:3836/respond?query=", URLencode(query))
    response <- GET(url)
    
    # Check if the response was successful
    if (status_code(response) != 200) {
      cat(paste("Error:", status_code(response), ":", http_status(response)), "\n")
      next  # Skip to the next question
    }
    
    # Parse the response as JSON
    content <- content(response, "parsed")
    
    # Output the response from Laptop 2
    print(content$response[[1]])
  }
}

# Run the querying agent with only 5 questions (to test)
querying_agent(questions[1:5])
