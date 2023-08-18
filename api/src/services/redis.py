from redis import Redis
from redis.commands.json.path import Path
from src.models import MovieCache
import json
import traceback
from typing import Dict


class Test:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def toJSON(self) -> str:
        return json.dumps({"id": self.id, "name": self.name})


class RedisClient:
    redis: Redis

    def __init__(self, host: str, port: int):
        self.redis = Redis(host="redis", port=6379)

    def addDocument(self, id, data):
        try:
            self.redis.json().set(id, Path.root_path(), data)
        except Exception as err:
            print("Error: ", err, flush=True)
            print(
                "Trace back: ",
                "".join(traceback.format_tb(err.__traceback__)),
                flush=True,
            )

    def getDocument(self, id) -> str:
        try:
            data = self.redis.json().get(id)
            return str(data)
        except Exception as err:
            print("Error: ", err, flush=True)
            return ""
        # try:
        #     data = self.redis.json().get(id)
        #     return dict(data)
        # except Exception as err:
        #     print("Error: ", err, flush=True)
