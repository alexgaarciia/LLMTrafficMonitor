import os
from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_ollama.chat_models import ChatOllama


###################################################
# API Keys
###################################################
# OpenAI
os.environ["OPENAI_API_KEY"] = ("sk-proj-o3z4d7s6BldQlc-x3vsWXCweUY55di21eL1WXt-52J2F5YHctH2_AU0i4-T3BlbkFJV"
                                "-j9rnTR4TD2giSrEolrkgCqdtUMqO8h2IsYtpGNzeKf3nJIGduBz2bBkA")
os.environ["ORGANIZATION_ID"] = "org-b9e6eTH4lj1kn4VhwdRfE1Rx"

# Mistral
os.environ["MISTRAL_API_KEY"] = "cgn4BLFLkeXPHAOfs16nhKDtgxUBDX7T"


###################################################
# Initialize the LLM with LangChain
###################################################
# Define the available models
MODELS = {
    "openai": OpenAI(temperature=0.9),
    "mistral": ChatMistralAI(),
    "gemma": ChatOllama(model="gemma2:27b"),
    "phi": ChatOllama(model="phi3:14b"),
    "local": OpenAI(base_url="http://localhost:3648/v1", api_key="lm-studio"),
}


###################################################
# Initialize Flask app
###################################################
app = Flask(__name__)
DEFAULT_MODEL = "phi"


@app.route('/respond', methods=['GET'])
def respond():
    # Get the query parameter from the request
    query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Get the selected model
    llm = MODELS.get(DEFAULT_MODEL)

    # Generate a response using the LLM
    try:
        response = llm.invoke(query)
    except Exception as e:
        return jsonify({"error": f"LLM invocation failed: {str(e)}"}), 500

    # Return the response
    print(f"Response from {DEFAULT_MODEL} model:", response.content)
    return jsonify({"response": response.content})


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)
