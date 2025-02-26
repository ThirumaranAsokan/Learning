from flask import Flask # type: ignore

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Python!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)