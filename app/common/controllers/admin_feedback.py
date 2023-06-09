from flask_restful import Resource
from app.common.models import  User, Appointment
from flask import jsonify ,session ,request
from app import db




class AdminFeedbackView(Resource):

    def post(self):
        if 'admin_id' not in session:
            response =  jsonify({'error': 'Unauthorized access.'})
            return response

        admin_id = session['admin_id']
        admin = User.query.filter_by(id=admin_id, is_admin=True).first()

        if not admin:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        # Get the appointment id from the request data
        data = request.get_json()
        appointment_id = data['appointment_id']
        admin_feedback = data['admin_feedback']

        # Retrieve the appointment from the database
        appointment = Appointment.query.get(appointment_id)

        if appointment:
            # Add the admin feedback to the appointment
            appointment.admin_feedback = admin_feedback
            db.session.commit()
            response = jsonify({'message': 'Feedback Submited successfully.'})
            return response
        else:
            response = jsonify({'error': 'Appointment not found.'})
            return response
