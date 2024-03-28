from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    token = fields.String(dump_only=True)

class UserMushroomSchema(Schema):
    name = fields.Str(required=True)
    image = fields.Raw(type='file')

class DetailUserMushroomSchema(Schema):
    name =  fields.Str()
    jenis_jamur =  fields.Str()
    path = fields.Str()
    isEdible= fields.Boolean()
    description = fields.Str()
    user_id = fields.Int(dump_only=True)

class GetUserMushroomSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    path = fields.Str()
    jenis_jamur = fields.Str()
    isEdible = fields.Str() 
    description = fields.Str()
    user_id = fields.Int(dump_only=True)



class EdibleSchema(Schema):
    id = fields.Int(dump_only=True)
    kalori = fields.Str()
    lemak = fields.Str()  
    karbohidrat = fields.Str()
    protein= fields.Str()
    mineral= fields.Str()
    vitamin= fields.Str()
    penggunaan_kuliner= fields.Str()
    manfaat_kesehatan= fields.Str()


class PredictEdibleUserMushroomSchema(EdibleSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    path = fields.Str()
    jenis_jamur = fields.Str()
    isEdible = fields.Str() 
    description = fields.Str()
    user_id = fields.Int(dump_only=True)
    content = fields.List(fields.Nested(EdibleSchema()), dump_only=True)

class InedibleSchema(Schema):
    id = fields.Int(dump_only=True)
    toksisitas = fields.Str()
    gejala = fields.Str()

class PredictInedibleUserMushroomSchema(InedibleSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    path = fields.Str()
    jenis_jamur = fields.Str()
    isEdible = fields.Str() 
    description = fields.Str()
    user_id = fields.Int(dump_only=True)
    content = fields.List(fields.Nested(InedibleSchema()), dump_only=True)

class MushroomSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    deskripsi = fields.Str()
    type = fields.Str()

class DetailMushroom(MushroomSchema):
    content = fields.List(fields.Nested(EdibleSchema()), dump_only=True)
