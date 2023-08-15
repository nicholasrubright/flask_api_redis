from marshmallow import Schema, fields
from src.models.movie import Movie, MovieSchema
from typing import List

class MovieCache:
    id: int
    movies: List[Movie]

    def __init__(self, id: int, movies: List[Movie]):
        self.id = id
        self.movies = movies

    def __repr__(self) -> str:
        return f"<MovieCache(id={self.id})>"

class MovieCacheSchema(Schema):
    id = fields.Int()
    movies = fields.Nested(MovieSchema, many=True)