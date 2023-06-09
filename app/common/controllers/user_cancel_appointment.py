from flask_restful import Resource
from app.common.models import User, Appointment
from flask import jsonify ,request, session
from app import db

# @app.route('/cancel_appointment', methods=['POST'])
class CancelAppointmentView(Resource):


    def post(self):
        data = request.get_json()

        # Check if user is authenticated
        if 'user_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).first()

        if not user:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        # Check if the appointment exists for the user
        appointment = Appointment.query.filter_by(id=data['appointment_id'], user_id=user_id, is_active=True).first()
        if not appointment:
            response = jsonify({'message': 'Invalid appointment id or appointment already cancelled.'})
            return response

        if appointment.is_visited:
            response = jsonify({'message': 'After visiting, you cannot cancel the appointment.'})
            return response

        appointment.is_active = False
        appointment.is_cancelled = True

        db.session.commit()

        response = jsonify({'message': 'Appointment cancelled successfully.'})
        return response


    
