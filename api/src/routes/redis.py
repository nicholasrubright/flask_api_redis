from flask import Blueprint
from http import HTTPStatus
from src.services import RedisClient
from src.models import MovieCache, Movie

redis_bp = Blueprint("redis_bp", __name__)


@redis_bp.route("/", methods=["GET"])
def get_redis(redisClient: RedisClient):
    try:
        redisClient.addDocument()
        return '', HTTPStatus.OK
    except:
        return "", HTTPStatus.INTERNAL_SERVER_ERROR
