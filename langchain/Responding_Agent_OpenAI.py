# OpenAI

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load environment variables
load_dotenv()


# OpenAI
from langchain_community.llms import OpenAI
from langchain_openai import OpenAI

os.environ[ "OPENAI_API_KEY"] = "your_key"
os.environ["ORGANIZATION_ID"] = "your_org_id"

# # Initialize Flask app
app = Flask(__name__)

# Initialize the LLM with LangChain
#llm = OpenAI(temperature=0.9) #OpenAI gpt-3.5-turbo-instruct
llm = OpenAI(model_name="gpt-4.5-preview-2025-02-27", temperature=0.9) # gpt-4.5


print(f"Using model: {llm.model_name}")
@app.route('/respond', methods=['GET'])
def respond():
    # Get the query parameter from the request
    query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Generate a response using the LLM
    try:
        response = llm.invoke(query)
        print(response)
    except Exception as e:
        return jsonify({"error": f"LLM invocation failed: {str(e)}"}), 500

    # Return the response as JSON
    # OpenAI
    print("2", jsonify({"response": response}))
    return jsonify({"response": response})


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)
     