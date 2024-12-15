import os
from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain_mistralai.chat_models import ChatMistralAI


###################################################
# Load environment variables
###################################################
# load_dotenv()


###################################################
# OpenAI
###################################################
os.environ["OPENAI_API_KEY"] = ("sk-proj-o3z4d7s6BldQlc-x3vsWXCweUY55di21eL1WXt-52J2F5YHctH2_AU0i4-T3BlbkFJV"
                                "-j9rnTR4TD2giSrEolrkgCqdtUMqO8h2IsYtpGNzeKf3nJIGduBz2bBkA")
os.environ["ORGANIZATION_ID"] = "org-b9e6eTH4lj1kn4VhwdRfE1Rx"
# Configure API key and organization ID from environment variables
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["ORGANIZATION_ID"] = os.getenv("ORGANIZATION_ID")


###################################################
# MistralAI
###################################################
os.environ["MISTRAL_API_KEY"] = "cgn4BLFLkeXPHAOfs16nhKDtgxUBDX7T"


###################################################
# Initialize Flask app
###################################################
app = Flask(__name__)


###################################################
# Initialize the LLM with LangChain
###################################################
# llm = OpenAI(temperature=0.9)  # OpenAI
# llm = ChatMistralAI()  # MistralAI
llm = OpenAI(base_url="http://localhost:3648/v1", api_key="lm-studio")  # LM Studio (Local Model)


@app.route('/respond', methods=['GET'])
def respond():
    # Get the query parameter from the request
    query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    # Generate a response using the LLM
    try:
        response = llm.invoke(query)
    except Exception as e:
        return jsonify({"error": f"LLM invocation failed: {str(e)}"}), 500

    # Return the response
    if isinstance(llm, OpenAI):
        print("Response from OpenAI/Local LLM:", response)
        return jsonify({"response": response})
    else:
        print(response.content)
        return response.content


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)
