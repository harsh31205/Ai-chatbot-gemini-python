from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    print("CHAT HIT")

    data = request.json

    user_message = data["message"]

    print("USER:", user_message)

    reply = get_response(user_message)

    print("BOT:", reply)

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)