from flask_restful import Api
from flask import Blueprint

from app.auth.controllers.login import LoginView
from app.auth.controllers.logout import LogoutView
from app.auth.controllers.users import UserView




auth_blueprint =Blueprint("auth",__name__,url_prefix="/auth")
api=Api(auth_blueprint)


# http://127.0.0.1:5000/api/auth/signup/
api.add_resource(UserView,"/user/") 
api.add_resource(LoginView,"/login/")
api.add_resource(LogoutView,"/logout/")