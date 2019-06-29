from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return jsonify({
        'status': 'ok...'
    })


@app.route('/api/userToProf')
def profile():
    return jsonify({
        'labels': ['JS', 'React', 'Node.js', 'CSS', 'HTML', 'Vue.js'],
        'datasets': [
            {
                'label': 'Your skills',
                'backgroundColor': 'rgba(13, 85, 255, 0.5)',
                'data': [40, 39, 10, 40, 39, 80]
            },
            {
                'label': 'Required skills',
                'backgroundColor': 'rgba(19, 189, 123, 0.5)',
                'data': [100, 100, 100, 100, 100, 100]
            }
        ]
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0')
