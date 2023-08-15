from marshmallow import fields, Schema

class Movie:
    id: int
    title: str

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()

