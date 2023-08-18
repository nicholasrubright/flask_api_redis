from marshmallow import Schema, fields
from src.models.movie import Movie, MovieSchema
from typing import List
from redis.commands.search.field import NumericField
import json


class MovieCache:
    id: int
    movies: List[Movie]

    def __init__(self, id: int, movies: List[Movie]):
        self.id = id
        self.movies = movies

    def toJSON(self):
        movie_json = []
        for movie in self.movies:
            movie_json.append(movie.toJSON())
        return json.dumps({'id': self.id, 'movies': movie_json})

    def __repr__(self) -> str:
        return f"<MovieCache(id={self.id})>"


class MovieCacheSchema(Schema):
    id = fields.Int()
    movies = fields.Nested(MovieSchema, many=True)


movie_cache_redis_schema = (
    NumericField('$.movie_cache.id', as_name='movie_cache')
)
