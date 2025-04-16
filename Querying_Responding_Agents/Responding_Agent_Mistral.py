import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Mistrail
from langchain_mistralai.chat_models import ChatMistralAI
os.environ["MISTRAL_API_KEY"] = "your_key"



# Initialize Flask app
app = Flask(__name__)

# Initialize the LLM with LangChain
llm = ChatMistralAI()  # Mistrail


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

    # Mistrail
    print(response.content)
    return response.content


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)


