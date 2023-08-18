from redis import Redis
from redis.commands.json.path import Path
from src.models.movie_cache import movie_cache_redis_schema
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
import ast
import json


class RedisClient:
    redis: Redis

    def __init__(self, host: str, port: int):
        self.redis = Redis(host=host, port=port)
        self._setSchemas()

    def _setSchemas(self):
        try:
            self.redis.ft().create_index(
                movie_cache_redis_schema,
                definition=IndexDefinition(
                    prefix=["movie_cache:"], index_type=IndexType.JSON
                ),
            )
        except Exception as err:
            print("Error occurred while setting json schemas: ", err, flush=True)

    def addJSONDocument(self, document_id: str, document: str):
        try:
            self.redis.json().set(document_id, Path.root_path(), document)
        except Exception as err:
            print("Error adding movie cache: ", err, flush=True)

    def getJSONDocument(self, document_id: str) -> str | None:
        try:
            data = self.redis.json().get(document_id)
            if len(data) > 0:
                data_as_json = ast.literal_eval(str(data))
                return json.dumps(data_as_json)

            print("There were multiple documents returned: ", data, flush=True)
            return None

        except Exception as err:
            print("Error getting json doc: ", err, flush=True)
            return None
