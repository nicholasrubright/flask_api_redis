from src.models import Movie, MovieSchema, MovieCache, MovieCacheSchema
from injector import inject

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