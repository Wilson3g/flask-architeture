from flask_architeture.extensions.marshmallow import marshmallow

class UserSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'email', 'name')

user_schema = UserSchema()
users_schema = UserSchema(many=True)