import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get(
        "GROQ_API_KEY", "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"
    )
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat_response():
    try:
        user_message = request.json.get("message")
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": user_message}],
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
