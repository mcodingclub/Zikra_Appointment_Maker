from flask_restful import Resource
from app import app
from flask import jsonify, session

# @app.route('/logout', methods=['POST'])
class LogoutView(Resource):

    def post(self):

        # Clear the user's session data
        session.clear()
        response = jsonify({'message': 'Logout successful.'})
        response.status_code= 200
        return response