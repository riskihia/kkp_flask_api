from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    token = fields.String(dump_only=True)

class EdibleSchema(Schema):
    id = fields.Int(dump_only=True)
    kalori = fields.Float()
    lemak = fields.Float()
    natrium  = fields.Float()   
    kalium  = fields.Float()    
    karbohidrat = fields.Float()

class InedibleSchema(Schema):
    id = fields.Int(dump_only=True)
    poison_name = fields.Str()
    amount = fields.Float()

class MushroomSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    type = fields.Str()

class DetailMushroom(MushroomSchema):
    content = fields.List(fields.Nested(EdibleSchema()), dump_only=True)
