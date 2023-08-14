from flask import Blueprint, jsonify
from http import HTTPStatus

movies_bp = Blueprint('movies_bp', __name__)

@movies_bp.route('/', methods=['GET'])
def get_movies():
    try:
        return jsonify({
            'movies': []
        }), HTTPStatus.OK
    except:
        return '', HTTPStatus.INTERNAL_SERVER_ERROR