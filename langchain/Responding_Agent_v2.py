import os
from flask import Flask, request, jsonify
from langchain_openai import OpenAI
from langchain_mistralai.chat_models import ChatMistralAI
from transformers import AutoTokenizer, AutoModelForCausalLM
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline


###################################################
# Load environment variables
###################################################
# load_dotenv()


###################################################
# OpenAI
###################################################
os.environ[
    "OPENAI_API_KEY"] = "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"
os.environ["ORGANIZATION_ID"] = "org-b9e6eTH4lj1kn4VhwdRfE1Rx"
# Configure API key and organization ID from environment variables
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
# os.environ["ORGANIZATION_ID"] = os.getenv("ORGANIZATION_ID")


###################################################
# MistralAI
###################################################
os.environ["MISTRAL_API_KEY"] = "cgn4BLFLkeXPHAOfs16nhKDtgxUBDX7T"


###################################################
# Qwen (QwQ-32B-Preview)
###################################################
tokenizer_qwen = AutoTokenizer.from_pretrained("Qwen/QwQ-32B-Preview")
model_qwen = AutoModelForCausalLM.from_pretrained("Qwen/QwQ-32B-Preview")
pipe_qwen = pipeline("text-generation", model=model_qwen, tokenizer=tokenizer_qwen)
qwen_llm = HuggingFacePipeline(pipeline=pipe_qwen)


###################################################
# Llama-3.3-70B
###################################################
tokenizer_llama = AutoTokenizer.from_pretrained("meta-llama/Llama-3.3-70B-Instruct")
model_llama = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.3-70B-Instruct")
pipe_llama = pipeline("text-generation", model=model_llama, tokenizer=tokenizer_llama)
llama_llm = HuggingFacePipeline(pipeline=pipe_llama)


###################################################
# Initialize Flask app
###################################################
app = Flask(__name__)


###################################################
# Initialize the LLM with LangChain
###################################################
# llm = OpenAI(temperature=0.9)  # OpenAI
llm = ChatMistralAI()  # MistralAI
# llm = qwen_llm  # Qwen
# llm = llama_llm  # Llama 


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
    # print("2", jsonify({"response": response}))
    # return jsonify({"response": response})

    # MistralAI
    print("2", response.content)
    return response.content


if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)
