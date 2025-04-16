import os
from flask import Flask, request, jsonify
    
from llamaapi import LlamaAPI
import json


api_token = 'your_key'

from langchain_core.prompts import ChatPromptTemplate


# Initialize Flask app
app = Flask(__name__)

@app.route('/respond', methods=['GET'])
def respond():
    # Get the query parameter from the request
    query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Initialize the LLM (stateless initialization for each query)
    try:
        llama = LlamaAPI(api_token)
        # API Request JSON Cell
        # API Request JSON Cell
        api_request_json = {
            "model": "llama3.1-70b",
           #"model": "llama3.2-11b-vision",	
            "messages": [
                #{"role": "system", "content": "You are a llama assistant that talks like a llama, starting every word with 'll'."},
                {"role": "user", "content": query},
            ]
        }

        response = llama.run(api_request_json)
        
                
        # Extract the assistant's message from the response
        assistant_message = response.json()["choices"][0]["message"]["content"]

        # Return the response as JSON
        return jsonify({"response": assistant_message})
    
    except Exception as e:
        return jsonify({"error": f"LLM invocation failed: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)