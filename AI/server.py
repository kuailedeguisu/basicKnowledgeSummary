from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/index")
def index():
    return jsonify(msg="Hello World")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8000)
