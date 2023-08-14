from typing import List
from marshmallow import fields, Schema
from redis_om import JsonModel, Field


class Movie:
    id: int
    title: str

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()


class MovieCache(JsonModel):
    id: int = Field(index=True, primary_key=True)
    movies: List[Movie]

    def __init__(self, id: int, movies: List[Movie]):
        self.id = id
        self.movies = movies


class MovieCacheSchema:
    id = fields.Int()
    movies = fields.Nested(MovieSchema, many=True)
