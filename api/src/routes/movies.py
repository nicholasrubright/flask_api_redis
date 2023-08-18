from flask import Blueprint, jsonify
from http import HTTPStatus
from src.services import MovieService, MovieCacheService
from src.models import Movie

movies_bp = Blueprint("movies_bp", __name__)


@movies_bp.route("/", methods=["GET"])
def get_movies(movieService: MovieService, movieCacheService: MovieCacheService):
    try:
        movieCacheService.createMovieCache(
            [Movie(1, "test movie"), Movie(2, "another test movie")]
        )
        data = movieService.getMovies()
        return data, HTTPStatus.OK
    except:
        return "", HTTPStatus.INTERNAL_SERVER_ERROR


@movies_bp.route("/test", methods=["GET"])
def get_movie_cache(movieCacheService: MovieCacheService):
    try:
        data = movieCacheService.getMovieCache(1)
        return jsonify(data), HTTPStatus.FOUND
    except:
        return "", HTTPStatus.INTERNAL_SERVER_ERROR
