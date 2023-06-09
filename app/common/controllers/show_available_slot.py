from flask_restful import Resource
from app.common.models import AvailableSlot ,User
from flask import jsonify , session


class GetAvailableSLotView(Resource):


    def get(self):
        if 'user_id' not in session and 'admin_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            response.status_code = 401
            return response

        is_admin = False
        if 'admin_id' in session:
            admin_id = session['admin_id']
            admin = User.query.filter_by(id=admin_id, is_admin=True).first()

            if admin:
                is_admin = True

        # Fetch available slots that are not booked
        available_slots = AvailableSlot.query.filter_by(is_cancelled=False, is_booked=False).all()

        slots_data = []
        for slot in available_slots:
            slot_data = {
                'id': slot.id,
                'admin_id': slot.admin_id,
                'datetime': slot.datetime.strftime('%d/%m/%Y , %I:%M %p'),
            }
            slots_data.append(slot_data)

        response_data = {'available_slots': slots_data}

        if is_admin:
            response_data['is_admin'] = True

            # # Query all available slots assigned to the admin that are not booked
            # admin_slots = AvailableSlot.query.filter_by(admin_id=admin_id, is_cancelled=False, is_booked=False).all()
            # admin_slots_data = []
            # for slot in admin_slots:
            #     slot_data = {
            #         'id': slot.id,
            #         'admin_id': slot.admin_id,
            #         'datetime': slot.datetime.strftime('%d/%m/%Y , %I:%M %p'),
            #     }
            #     admin_slots_data.append(slot_data)

            # # response_data['admin_slots'] = admin_slots_data

        response = response_data
        return response
