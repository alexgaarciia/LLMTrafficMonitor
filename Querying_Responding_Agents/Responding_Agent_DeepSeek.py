
 ################################################################ v8 Depseek
 
 
import os
from flask import Flask, request, jsonify
from openai import OpenAI
import json

# Initialize OpenAI client for DeepSeek
client = OpenAI(
    api_key="your_key",
    base_url="https://api.deepseek.com"
)

# Initialize Flask app
app = Flask(__name__)

@app.route('/respond', methods=['GET'])
def respond():
    # Get the query parameter from the request
    query = request.args.get('query', '')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        # Construct the request payload
        response = client.chat.completions.create(
            model="deepseek-reasoner", # DeepSeek-R1
            # model="deepseek-chatr", # DeepSeek-V3
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": query}
            ],
            stream=False
        )

        # Extract the assistant's message
        assistant_message = response.choices[0].message.content

        # Return the response as JSON
        return jsonify({"response": assistant_message})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"LLM invocation failed: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(port=3836, debug=True)

