from redis import Redis
from redis.commands.json.path import Path
from src.models.movie_cache import movie_cache_redis_schema
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from src.models.movie_cache import MovieCache

# class Test:
#     def __init__(self, id: int, name: str):
#         self.id = id
#         self.name = name

#     def toJSON(self) -> str:
#         return json.dumps({"id": self.id, "name": self.name})


class RedisClient:
    redis: Redis

    def __init__(self, host: str, port: int):
        self.redis = Redis(host="redis", port=6379)

    def _setSchemas(self):
        self.redis.ft().create_index(movie_cache_redis_schema, definition=IndexDefinition(
            prefix=['movie_cache:'], index_type=IndexType.JSON))

    def addMovieCache(self, movieCache: MovieCache):
        try:
            self.redis.json().set(str(movieCache.id), Path.root_path(), movieCache.toJSON())
        except Exception as err:
            print("Error adding movie cache: ", err, flush=True)

    # def addDocument(self, id, data):
    #     try:
    #         self.redis.json().set(id, Path.root_path(), data)
    #     except Exception as err:
    #         print("Error: ", err, flush=True)
    #         print(
    #             "Trace back: ",
    #             "".join(traceback.format_tb(err.__traceback__)),
    #             flush=True,
    #         )

    def getDocument(self, id) -> str:
        try:
            data = self.redis.json().get(id)
            return str(data)
        except Exception as err:
            print("Error: ", err, flush=True)
            return ""
