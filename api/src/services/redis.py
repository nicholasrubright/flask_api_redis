from redis import Redis
from redis.commands.json.path import Path
from src.models import MovieCache


# class RedisClient:
#     redis: Redis

#     def __init__(self, host: str, port: int):
#         self.redis = Redis(host=host, port=port)

#     def addDocument(self, cache: MovieCache):
#         self.redis.json().set(f"cache{cache.id}", Path.root_path(), cache)
