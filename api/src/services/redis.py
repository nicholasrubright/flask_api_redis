from redis import Redis
from redis.commands.json.path import Path
from src.models.movie_cache import movie_cache_redis_schema
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
import json


class RedisClient:
    redis: Redis

    def __init__(self, host: str, port: int):
        self.redis = Redis(host="redis", port=6379)
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
            print("testing doc_id: ", document_id, flush=True)
            print("testing doc: ", document, flush=True)
            self.redis.json().set(document_id, Path.root_path(), document)
        except Exception as err:
            print("Error adding movie cache: ", err, flush=True)

    def getJSONDocument(self, document_id: str) -> str:
        try:
            data = self.redis.json().get(document_id)

            print("data from getJSONDocument: ", data, flush=True)
            data_json = data.replace("'", '"')
            print("data json: ", data_json, flush=True)
            return str(data_json)
        except Exception as err:
            print("Error: ", err, flush=True)
            return ""
