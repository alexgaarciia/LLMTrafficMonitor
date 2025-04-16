import os
from flask import Flask, request, jsonify

os.environ["GROQ_API_KEY"]= "your_key"

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

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
        llm = ChatGroq(model_name="qwen-2.5-32b")
        response = llm.invoke(query)  # Process the query
    except Exception as e:
        return jsonify({"error": f"LLM invocation failed: {str(e)}"}), 500

    # Return the response as JSON
    return jsonify({"response": response.content})  # Convert to JSON and send back


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)
     