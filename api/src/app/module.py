from flask import Flask
from injector import Module, singleton
from src.services import MovieService, MovieCacheService
from src.models import MovieCacheSchema, MovieSchema


class AppModule(Module):
    def __init__(self, app: Flask):
        self.app = app

    def configure(self, binder):
        binder.bind(MovieSchema, to=self.getMovieSchema(), scope=singleton)
        binder.bind(MovieCacheSchema, to=self.getMovieCacheSchema(), scope=singleton)

        binder.bind(MovieService, to=self.getMovieService(), scope=singleton)
        binder.bind(MovieCacheService, to=self.getMovieCacheService(), scope=singleton)

    def getMovieSchema(self) -> MovieSchema:
        return MovieSchema()

    def getMovieCacheSchema(self) -> MovieCacheSchema:
        return MovieCacheSchema()

    def getMovieService(self) -> MovieService:
        return MovieService(self.getMovieSchema())

    def getMovieCacheService(self) -> MovieCacheService:
        return MovieCacheService(self.getMovieCacheSchema())
