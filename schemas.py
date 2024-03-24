from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    token = fields.String(dump_only=True)


class MushroomSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    type = fields.Str()
