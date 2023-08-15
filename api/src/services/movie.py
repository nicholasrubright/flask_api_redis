from src.models import Movie, MovieSchema, MovieCache, MovieCacheSchema
from injector import inject
from redis import Redis
test_movies = [Movie(1, "test movie"), Movie(2, "another test movie")]

# Notes: https://redis.readthedocs.io/en/stable/examples/search_json_examples.html
# Movie Cache
class MovieCacheService:
    @inject
    def __init__(self, movieCacheSchema: MovieCacheSchema, redis: Redis):
        self.movieCacheSchema = movieCacheSchema
        self.redis = redis

    def createMovieCache(self, movies):
        try:
            movieCache = MovieCache(1, movies)
            print("testing: ", movieCache, flush=True)
            data = self.movieCacheSchema.dump(movieCache)
            print("test: ", str(movieCache.id), flush=True)
            self.redis.set(str(movieCache.id), str(data))
        except Exception as err:
            print("There was a problem creating the cache: ", err, flush=True)


# Main movie service
class MovieService:
    @inject
    def __init__(self, movieSchema: MovieSchema):
        self.movieSchema = movieSchema

    def getMovies(self):
        movies = self.movieSchema.dump(test_movies, many=True)
        return movies
