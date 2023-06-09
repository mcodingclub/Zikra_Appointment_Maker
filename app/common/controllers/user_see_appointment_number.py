from flask_restful import Resource
from app.common.models import AvailableSlot , User, Appointment
from flask import jsonify ,session


# @app.route('/appointments', methods=['GET'])
class GetAppointmentView(Resource):

    def get(self):
   
        if 'user_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        user_id = session['user_id']
        user = User.query.filter_by(id=user_id).first()

        if not user:
            response =  jsonify({'error': 'Unauthorized access.'})
            return response 

        # Get all the appointments for the user
        appointments = Appointment.query.filter_by(user_id=user_id).all()

        
        appointment_details = []

        
        for appointment in appointments:
            available_slot = AvailableSlot.query.filter_by(id=appointment.available_slot_id).first()

            if available_slot:
                appointment_detail = {
                    'id': appointment.id,
                    'datetime': available_slot.datetime,
                    'is_visited': appointment.is_visited,
                    'is_active': appointment.is_active
                }

                appointment_details.append(appointment_detail)

        response = jsonify({'appointment': appointment_details})
        return response

