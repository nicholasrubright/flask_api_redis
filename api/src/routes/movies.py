from flask import Blueprint
from http import HTTPStatus
from src.services import MovieService, MovieCacheService
from src.models import Movie

movies_bp = Blueprint("movies_bp", __name__)


@movies_bp.route("/", methods=["GET"])
def get_movies(movieService: MovieService):
    try:

        # movieCacheService.createMovieCache([Movie(1, "test movie"), Movie(2, "another test movie")])
        data = movieService.getMovies()
        return data, HTTPStatus.OK
    except:
        return "", HTTPStatus.INTERNAL_SERVER_ERROR
