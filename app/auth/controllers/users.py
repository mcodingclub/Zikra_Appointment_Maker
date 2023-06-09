from flask import  request, jsonify
from flask_restful import Resource 
from app import app ,db
from app.common.models import User
from sqlalchemy.exc import IntegrityError



class UserView(Resource):
    
    def post(self):
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        is_admin = data.get('is_admin', False)

        user = User(username=username, email=email, password=password, is_admin=is_admin)
        try:
                db.session.add(user)
                db.session.commit()
                response = jsonify({'message': 'User added successfully'})
                response.status_code = 201
                return response
        except IntegrityError:
                db.session.rollback()
                response = jsonify({'error': 'User already exists'})
                response.status_code = 400
                return response