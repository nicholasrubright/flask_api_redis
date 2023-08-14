from flask import Blueprint, jsonify
from http import HTTPStatus
from src.services import MovieService, MovieCacheService

movies_bp = Blueprint("movies_bp", __name__)


@movies_bp.route("/", methods=["GET"])
def get_movies(movieService: MovieService):
    try:
        data = movieService.getMovies()
        return data, HTTPStatus.OK
    except:
        return "", HTTPStatus.INTERNAL_SERVER_ERROR
