import secrets
from flask_login import LoginManager
from flask_restful import Resource
from app import app
from app.common.models import User
from flask import  request, jsonify , session

login_manager = LoginManager(app)
login_manager.init_app(app)


login_manager.login_view = 'login'



# Generate a secure random string to use as the secret key
secret_key = secrets.token_hex(16)  # 16 bytes (128 bits) of random data


# Set the secret key in your Flask application
app.secret_key = secret_key

@login_manager.user_loader
def load_user(user_id):
    # Load the user from the database based on their ID
    return User.query.get(int(user_id))



# @app.route('/login', methods=['POST'])
class LoginView(Resource):
    
    def post(self):

        username = request.json.get('username')
        password = request.json.get('password')
        user = User.query.filter_by(username=username).first()

        if not user or not user.password == password:
            response =  jsonify({'message': 'Invalid username or password'})
            response.status_code = 401
            return response

        # Check if the user is an admin or a regular user
        if user.is_admin:
            # Set the admin_id value in the session
            session['admin_id'] = user.id
        else:
            # Set the user_id value in the session
            session['user_id'] = user.id
        response=jsonify({'message': 'Login successful'})
        response.status_code = 200

        return  response