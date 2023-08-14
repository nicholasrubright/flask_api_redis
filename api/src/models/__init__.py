from typing import List
from marshmallow import fields, Schema

class Movie:
    id: int
    title: str
    
    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title
        
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    
    
    
class MovieCache:
    id: int
    movies: List[Movie]
    
    def __init__(self, id: int, movies: List[Movie]):
        self.id = id
        self.movies = movies
    
class MovieCacheSchema:
    
    id = fields.Int()
    movies = fields.Nested(MovieSchema, many=True)