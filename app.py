from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({
        'status': 'ok...'
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
