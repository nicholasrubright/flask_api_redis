from marshmallow import fields, Schema
import json


class Movie:
    id: int
    title: str

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def toJSON(self):
        return json.dumps({'id': self.id, 'title': self.title})


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
