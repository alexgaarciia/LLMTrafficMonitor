



This dataset contains network traffic captures and analysis for 7 different LLMs:

1.MistralAI
2.Claude-3-sonnet
3.llama3.1-70b
4.llama3.2-11b-vision
5.Groq (qwen-2.5-32b)
6.Openai gpt-4o
7.Deepseek (only tested locally using ollama)

Folder Structure

Each model has its own folder containing:
- Wireshark capture files (.pcapng) with all packets.
- Exported CSV files with filtered packets for analysis.

The Stream index column shows individual requests and their corresponding responses.
Each request/response pair is assigned a unique stream index.


- Folder packet_stream_sizes: 
This folder includes packet size data for each request and response after processing the data (from other 7 folders). Each benchmark question corresponds to a separate stream:
	-request_response_separate/ – contains separate packet size data for requests and responses.
	- request+response/ – contains the total packet size (request + response) for each stream.



Wireshark Display Filters (by IP Address)
Use the following filters to isolate traffic for each model in Wireshark:

#mistral
ip.addr ==104.18.23.152  || ip.addr ==104.18.22.152 

#openai
ip.addr == 162.159.140.245 || ip.addr == 172.66.0.243 

#Groq 
ip.addr == 104.18.3.205 || ip.addr == 104.18.2.205

#llama 3.1
ip.addr == 188.114.97.5 || ip.addr == 188.114.96.5

#llama 3.2 
ip.addr == 172.67.214.125 || ip.addr == 188.114.97.5 || ip.addr == 188.114.96.5 || ip.addr == 104.21.86.38

#Claude
ip.addr == 160.79.104.10

#deepseek
#ip.addr == 104.18.26.90


Localhost:
ip.addr ==127.0.0.1 && tcp.port ==3836






