from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Coloca tu API Key de OpenAI aquí
openai.api_key = "TU_API_KEY_AQUI"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
