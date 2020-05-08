from flask import abort, jsonify, request
from flask_restful import Resource
from flask_architeture.models.file import File, db
from flask_architeture.schema.file_schema import file_schema, files_schema 

import datetime
import os


class FileResource(Resource):
    def get(self):
        try:
            files = File.query.all()

            if not files:
                return {'success': False, 'message': 'Nenhum usuário encontrado'}

            return {'success': True, 'data': files_schema.dump(files)}
        except:
            return {'success': False, 'message': 'Erro ao buscar usuários'}

    def post(self):
        try:
            if 'file' not in request.files:
                return {'success': False, 'message': 'Nenhum arquivo enviado'}, 500

            file = request.files['file']

            if file.filename == '':
                return {'success': False, 'message': 'Nenhum arquivo enviado'}, 500

            allowed_file = '.' in file.filename and \
                file.filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

            if file and allowed_file:
                hased_name = str(datetime.datetime.now().timestamp())+'.pdf'
 
                new_file = File(file.filename, hased_name)
                db.session.add(new_file)
                db.session.commit()
                
                file.save(os.path.join('storage', hased_name))

                return {'success': True, 'message': file_schema.dump(new_file)}, 200
            else:
                return {'success': False, 'message': 'Informe uma extensão de arquivo válida'}, 500
        except:
            return {'success': False, 'message': 'Erro ao salvar arquivo'}, 200


class FileItemResource(Resource):
    def delete(self, file_id):
        try:
            file = File.query.get(file_id)

            if not file:
                return {'success': False, 'message': 'Nenhum arquivo encontrado'}, 404

            db.session.delete(file)
            db.session.commit()

            return {'success': True, 'message': 'Arquivo deletado'}, 200
        except:
            return {'success': False, 'message': 'Erro ao excluir'}, 500

    def get(self, file_id):
        try:
            file = File.query.get(file_id)

            if not file:
                return {'success': False, 'message': 'Nenhum arquivo encontrado'}, 404

            return {'success': True, 'data': file_schema.dump(file)}
        except:
            return {'success': False, 'message': 'Erro ao buscar arquivos'}, 404