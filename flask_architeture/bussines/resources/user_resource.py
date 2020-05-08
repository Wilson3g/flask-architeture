from flask import abort, jsonify, request
from flask_restful import Resource
from flask_architeture.models.user import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_architeture.schema.user_schema import users_schema, user_schema

import string
import random


class UserResource(Resource):
    def get(self):
        try:
            all_users = User.query.all()
            result = users_schema.dump(all_users)

            return {'message': True, 'data': result}, 200
        except:
            return {'success': False, 'message': 'Nenhum usuário encontrado'}

    def post(self):
        if len(request.json) < 3 or '' in request.json.values():
            return {'message': 'todos os dados devem ser informados!', 'success': False}

        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        if User.query.filter_by(email=email).first():
            return {'message': 'Email já cadastrado'}

        try:
            pass_hash = generate_password_hash(password)
            user = User(name, email, pass_hash)
            db.session.add(user)
            db.session.commit()

            return {'success':True, 'data': user_schema.dump(user)}
        except:
            return {'success':False, 'message': 'Não foi possível registrar'}

class UserItemResource(Resource):
    def get(self, id):
        
        try:
            user = User.query.get(id)

            if not user:
                return {'message': 'Usuário inexistente'}, 404
            
            return {'success': True, 'data': user_schema.dump(user)}
        except:
            return {'success': False, 'message': 'Usuário não encontrado'}


    def delete(self, id):
        user = User.query.get(id)

        if not user:
            return {'message': 'Usuário não existe'}, 404

        try:
            db.session.delete(user)
            db.session.commit()

            return {'success': True,'message': 'Usuário deletado'}, 200
        except:
            return {'message': 'Não foi possível deletar'}


    def put(self, id):

        if len(request.json) < 3 or '' in request.json.values():
            return {'message': 'todos os dados devem ser informados!', 'success': False}

        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        user = User.query.get(id)

        if not user:
            return {'message': 'Usuário inexistente'}, 404

        pass_hash = generate_password_hash(password)

        try:
            user.name = name
            user.email = email
            user.password = pass_hash

            db.session.commit()

            return {'message': 'Usuário atualizado com sucesso', 'data': user_schema.dump(user)}, 201
        except:
            return {'message': 'Não foi possível atualizar o usuário'}
