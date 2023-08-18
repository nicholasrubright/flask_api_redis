from redis import Redis
from redis.commands.json.path import Path
from src.models import MovieCache
import json
import traceback


class Test:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def toJSON(self) -> str:
        return json.dumps({'id': self.id, 'name': self.name})


class RedisClient:
    redis: Redis

    def __init__(self, host: str, port: int):
        self.redis = Redis(host='redis', port=6379)

    def addDocument(self):
        try:

            test_obj = Test(99, 'test name')
            print("testing: ", test_obj, flush=True)
            data = test_obj.toJSON()
            print("Testing again: ", data, flush=True)
            self.redis.json().set(name='test:99',
                                  path=Path.root_path(), obj=str(data))
        except Exception as err:
            print("Error: ", err, flush=True)
            print("Trace back: ", ''.join(
                traceback.format_tb(err.__traceback__)), flush=True)
