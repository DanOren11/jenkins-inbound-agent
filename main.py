from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_api():
    """Returns a JSON greeting."""
    return jsonify({"message": "Hello from the API!"})

if __name__ == "__main__":
    app.run(debug=True)
