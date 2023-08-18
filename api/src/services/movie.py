from src.models import Movie, MovieSchema, MovieCache, MovieCacheSchema
from injector import inject
from src.services.redis import RedisClient
import json

test_movies = [Movie(1, "test movie"), Movie(2, "another test movie")]


# Notes: https://redis.readthedocs.io/en/stable/examples/search_json_examples.html
# Movie Cache
class MovieCacheService:
    @inject
    def __init__(self, movieCacheSchema: MovieCacheSchema, redis: RedisClient):
        self.movieCacheSchema = movieCacheSchema
        self.redis = redis

    def createMovieCache(self, movies):
        try:
            movieCache = MovieCache(1, movies)
            data = self.movieCacheSchema.dump(movieCache)
            self.redis.addJSONDocument(str(movieCache.id), str(data))
        except Exception as err:
            print("There was a problem creating the cache: ", err, flush=True)

    def getMovieCache(self, id: str):
        try:
            data = self.redis.getJSONDocument(id)
            print("get movie cache json: ", data, flush=True)
            data_obj = json.loads(data)
            print("data_obj: ", data_obj, flush=True)
            movieCache = self.movieCacheSchema.load(data_obj)
            return movieCache
        except Exception as err:
            print("Error getting movie cache: ", err, flush=True)


# Main movie service
class MovieService:
    @inject
    def __init__(self, movieSchema: MovieSchema):
        self.movieSchema = movieSchema

    def getMovies(self):
        movies = self.movieSchema.dump(test_movies, many=True)
        return movies
