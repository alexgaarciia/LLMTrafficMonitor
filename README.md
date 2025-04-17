# LLMTrafficMonitor 
The main goal of this repository is to capture how much traffic do LLMs generate. 

## Key folders and files in the repository
### Folder: R_running_locally
- responding_agent.R: Implements a responding agent, which processes incoming queries using an local LLM. The script defines a Plumber API endpoint to handle requests, respond to queries, and simulate conversational interactions.
- querying_agent.R: Implements a querying agent that repeatedly prompts the user for a query (until 'Exit' is typed), sends it to a responding agent via an HTTP request, and displays the response.
- querying_agent_math.R: Extracts a set of questions from a JSONL file, then sends these questions to the responding agent via HTTP requests. The querying agent processes the responses for each question and prints the results. 

### Folder: langchain
- Responding_Agent_v2.py: Implements a Flask-based server that handles queries and generates responses using LangChain models.
- Querying_Agent_v2_json.py: Sends queries to a LangChain model, processes responses, and measures request and response sizes.
- langchain_demo.ipynb: Jupter notebook used to test out the LangChain library.

### Folder: packet_capture
- scapy_packet_capture_demo.ipynb: Jupyter notebook that captures packets based on a target IP and port, then prints details about the source and destination IPs, ports, and packet size.
- packet_capture_v2.py: Python script that captures network packets based on a target IP and port, then prints details about the packets.

### Folder: data
- test.jsonl: JSON file containing math questions (obtained from [OpenAI](https://github.com/openai/grade-school-math/tree/master)).


## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.


## License
This project is licensed under the MIT License. See the [LICENSE]() file for more details.


## References
> **Introducing Large Language Models as the Next Challenging Internet Traffic Source**
> 
> Nataliia Koneva, Alejandro Leonardo García Navarro, Alfonso Sánchez-Macián, José Alberto Hernández, Moshe Zukerman, Óscar González de Dios
> 
> *URL:* [https://arxiv.org/abs/2504.10688](https://arxiv.org/abs/2504.10688)
