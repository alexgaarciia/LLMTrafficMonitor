

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from langchain_anthropic import ChatAnthropic

# Load environment variables
load_dotenv()

# Set API key directly (if not using .env)
os.environ["ANTHROPIC_API_KEY"] = "your_key"

# Initialize Claude LLM
llm = ChatAnthropic(model="claude-3-sonnet-20240229") # temp = 0.7

# Flask app setup
app = Flask(__name__)

@app.route('/respond', methods=['GET'])
def respond():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        response = llm.invoke(query)
        print("Response:", response)
        return jsonify({"response": response.content})  # FIXED: get just the text
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3836, debug=True)