from flask import Flask

app = Flask(__name__)

@app.route("/books")
def books():
    reply = "{ books : {'book 1': 5, 'book 2': 3, 'book 3': 3} }"
    return reply

@app.route("/")
def index():
    return "It Works!!!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082, debug=True)

