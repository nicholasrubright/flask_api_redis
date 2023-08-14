from src.models import Movie, MovieSchema, MovieCache, MovieCacheSchema
from injector import inject

test_movies = [Movie(1, "test movie"), Movie(2, "another test movie")]


# Movie Cache
class MovieCacheService:
    @inject
    def __init__(self, movieCacheSchema: MovieCacheSchema):
        self.movieCacheSchema = movieCacheSchema


# Main movie service
class MovieService:
    @inject
    def __init__(self, movieSchema: MovieSchema):
        self.movieSchema = movieSchema

    def getMovies(self):
        movies = self.movieSchema.dump(test_movies, many=True)
        return movies
