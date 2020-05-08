from flask_architeture.extensions.marshmallow import marshmallow

class FileSchema(marshmallow.Schema):
    class Meta:
        fields = ('name', 'path_file')

file_schema = FileSchema()
files_schema = FileSchema(many=True)