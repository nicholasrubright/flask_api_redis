from http import HTTPStatus
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def test():
    return jsonify({
        'hello': 'world'
    }), HTTPStatus.OK
    
app.run('0.0.0.0', port=8080)