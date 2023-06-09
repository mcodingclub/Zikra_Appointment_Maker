from flask_restful import Resource
from app.common.models import  User, Appointment
from flask import jsonify ,session ,request
from app import db


class VisitedAppointmentView(Resource):

    

    def put(self):
        data = request.get_json()

        # Check if admin is authenticated
        if 'admin_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        admin_id = session['admin_id']
        admin = User.query.filter_by(id=admin_id, is_admin=True).first()

        if not admin:
            response= jsonify({'error': 'Unauthorized access.'})
            return response

        appointment_id = data.get('appointment_id')

        # Check if the appointment exists
        appointment = Appointment.query.filter_by(id=appointment_id).first()

        if not appointment:
            response = jsonify({'error': 'Invalid appointment id.'})
            return response

    
        appointment.is_visited = True

        db.session.commit()

        response = jsonify({'message': 'User Visited successfully.'})
        return response
