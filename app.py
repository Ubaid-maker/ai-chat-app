import os
from flask import Flask, jsonify, request
from groq import Groq

app = Flask(__name__)

# Initialize Groq client using environment variable
client = Groq(api_key=os.environ.get("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"))

@app.route('/')
def home():
    return jsonify({"message": "Flask app deployed successfully on Vercel!"})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("prompt", "")

    if not user_input:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[{"role": "user", "content": user_input}]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
