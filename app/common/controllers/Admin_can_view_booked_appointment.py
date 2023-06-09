from flask_restful import Resource
from flask import  jsonify , session 
from app.common.models import User ,Appointment ,AvailableSlot


class AdminCanShowBookedAppointmentView(Resource):

      def get(self):
        if 'admin_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        admin_id = session['admin_id']
        admin = User.query.filter_by(id=admin_id, is_admin=True).first()

        if not admin:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        appointments = Appointment.query.filter_by(is_active=True).all()

        appointment_data = []
        for appointment in appointments:
            user = User.query.filter_by(id=appointment.user_id).first()
            slot_id = appointment.available_slot_id
            slot = AvailableSlot.query.filter_by(id=slot_id).first()

            if slot:
                appointment_info = {
                    'appointment_id': appointment.id,
                    'user_id': user.id,
                    'user_name': user.username,  
                    'slot_id': slot_id,
                    'datetime': slot.datetime.strftime('%d/%m/%Y , %I:%M %p')
                }
                appointment_data.append(appointment_info)

        response_data = {
            'appointments': appointment_data,
            'total_appointments': len(appointment_data)
        }

        response = jsonify(response_data)
        return response







    # def get(self):
    
    #     if 'admin_id' not in session:
    #         response = jsonify({'error': 'Unauthorized access.'})
    #         response.status_code = 401
    #         return response

    #     admin_id = session['admin_id']
    #     admin = User.query.filter_by(id=admin_id, is_admin=True).first()

    #     if not admin:
    #         response = jsonify({'error': 'Unauthorized access.'})
    #         response.status_code = 401
    #         return response

    #     slot_counts = db.session.query(Appointment.available_slot_id, func.count(Appointment.id)).group_by(Appointment.available_slot_id).all()

    #     slots_data = []
    #     for slot_id, count in slot_counts:
    #         slot_data = {
    #             'slot_id': slot_id,
    #             'num_appointments': count  # Number of appointments booked for each slot
    #         }
    #         slots_data.append(slot_data)

    #     response_data = {'slots_data': slots_data}

    #     response = jsonify(response_data)
    #     return response