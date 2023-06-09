from flask_restful import Resource
from app.common.models import Appointment ,AvailableSlot
from flask import jsonify, session

class ViewAdminFeedbackView(Resource):

    def get(self):
        if 'user_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        user_id = session['user_id']
        appointments = Appointment.query.filter_by(user_id=user_id).all()

        feedback_data = []
        for appointment in appointments:
            available_slot = AvailableSlot.query.filter_by(id=appointment.available_slot_id).first()
            feedback = {
                'date': available_slot.datetime.date().isoformat(),
                'feedback': appointment.admin_feedback
            }
            feedback_data.append(feedback)

        if feedback_data:
            response = jsonify({'feedback': feedback_data})
            return response
        else:
            response = jsonify({'message': 'No admin feedback available.'})
            return response