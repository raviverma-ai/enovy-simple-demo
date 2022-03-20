from flask import Flask

app = Flask(__name__)

@app.route("/stationaries")
def stationay():
    reply = "{ stationaries: { pens : {'Pen type 1': 7, 'Pen type 2': 2, 'Pen type 3': 3}, registers: {'type 1' : 4, 'type 2' : 3, 'type 3' : 0} } }"
    return reply

@app.route("/")
def index():
    return "It Works!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)

