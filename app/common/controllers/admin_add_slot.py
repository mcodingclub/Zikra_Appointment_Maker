from flask_restful import Resource
from flask import  request, jsonify , session
from app.common.models import User , AvailableSlot
from datetime import datetime
from datetime import date
from app import db




class AddSlotView(Resource):
    
     def post(self):
        data = request.get_json()

        
        if 'admin_id' not in session:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        admin_id = session['admin_id']
        admin = User.query.filter_by(id=admin_id, is_admin=True).first()

        if not admin:
            response = jsonify({'error': 'Unauthorized access.'})
            return response

        slot_datetime = datetime.strptime(data['datetime'], '%d/%m/%Y , %I:%M %p')
        current_date = date.today()

        # Check if the slot date is in the past
        if slot_datetime.date() < current_date:
            response = jsonify({'message': 'You cannot book a slot for a previous date.'})
            return response

        new_slot = AvailableSlot(admin_id=admin_id, datetime=slot_datetime, is_cancelled=data['is_cancelled'])

        # Check if slot already exists
        existing_slot = AvailableSlot.query.filter_by(admin_id=admin_id, datetime=new_slot.datetime).first()
        if existing_slot:
            response = jsonify({'message': 'This slot already exists.'})
            return response

        db.session.add(new_slot)
        db.session.commit()

        response = jsonify({'message': 'Slot added successfully.'})
        return response




    