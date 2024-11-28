## Key folders and files in the repository
### Folder: R_running_locally
This folder contains R scripts for locally running the querying and responding agents, designed to communicate with a local LLM.
- responding_agent.R: Implements a responding agent, which processes incoming queries using an open-source model from LM Studio. The script defines a Plumber API endpoint to handle requests, respond to queries, and simulate conversational interactions.
- querying_agent.R: Implements a querying agent that repeatedly prompts the user for a query (until 'Exit' is typed), sends it to a responding agent via an HTTP request, and displays the response.
- querying_agent_math.R: This script extracts a set of questions from a JSONL file, then sends these questions to the responding agent via HTTP requests. The querying agent processes the responses for each question and prints the results. 

### Folder: langchain
- Querying_Agent_v2_json.py:
- Responding_Agent_v2.py:
- langchain_demo.ipynb

### Folder: data


### Folder: packet_capture
