from flask import  request, jsonify , session
from flask_restful import Resource
from app.common.models import User , AvailableSlot, Appointment
from app import db


class BookAppointmentView(Resource):

   def post(self):
    data = request.get_json()

    if 'user_id' not in session:
        response = jsonify({'error': 'Unauthorized access.'})
        return response

    user_id = session['user_id']
    user = User.query.filter_by(id=user_id).first()

    if not user:
        response = jsonify({'error': 'Unauthorized access.'})
        return response

    # Check if the user has visited or their previous appointment is canceled
    previous_appointment = Appointment.query.filter_by(user_id=user_id).order_by(Appointment.id.desc()).first()
    if previous_appointment and not previous_appointment.is_visited and previous_appointment.is_active:
        response = jsonify({'message': 'You cannot book another appointment until you have visited or your previous appointment is canceled.'})
        return response

    # Check if the appointment already exists for the user and date
    existing_appointment = Appointment.query.filter_by(user_id=user_id, available_slot_id=data['available_slot_id']).first()
    if existing_appointment:
        response = jsonify({'message': 'This appointment already exists.'})
        return response

    available_slot = AvailableSlot.query.filter_by(id=data['available_slot_id']).first()

    if not available_slot:
        response = jsonify({'message': 'Invalid available slot id.'})
        return response

    if available_slot.is_cancelled:
        response = jsonify({'message': 'This slot is cancelled.'})
        return response

    new_appointment = Appointment(user_id=user_id,
                                  available_slot_id=data['available_slot_id'],
                                  is_visited=False,
                                  is_active=True)

    # Set the datetime value for the new appointment
    new_appointment.datetime = available_slot.datetime

    db.session.add(new_appointment)

    # Mark the available slot as booked
    available_slot.is_booked = True

    db.session.commit()

    response = jsonify({'message': 'Appointment added successfully.'})
    return response



        # def post(self):

        # data = request.get_json()

        
        # if 'user_id' not in session:
        #     response = jsonify({'error': 'Unauthorized access.'})
        #     return response

        # user_id = session['user_id']
        # user = User.query.filter_by(id=user_id).first()

        # if not user:
        #     response = jsonify({'error': 'Unauthorized access.'})
        #     return response 

        # # Check if the appointment already exists for the user and date
        # existing_appointment = Appointment.query.filter_by(user_id=user_id, available_slot_id=data['available_slot_id']).first()
        # if existing_appointment:
        #     response = jsonify({'message': 'This appointment already exists.'})
        #     return response

        
        # available_slot = AvailableSlot.query.filter_by(id=data['available_slot_id']).first()

        # if not available_slot:
        #     response = jsonify({'message': 'Invalid available slot id.'})
        #     return response

        # if available_slot.is_cancelled:
        #     response = jsonify({'message': 'This slot is cancelled.'})
        #     return response

        # appointments_on_date = Appointment.query.filter_by(user_id=user_id).filter(func.date(AvailableSlot.datetime) == func.date(available_slot.datetime)).all()

        # for appointment in appointments_on_date:
        #     if appointment.is_active and not available_slot.is_cancelled:
        #         response = jsonify({'message': 'You cant book appointment until its getting cancel or you can visit'})
        #         return response

        # # Check if the appointment is already booked by someone else
        # appointment_by_other_user = Appointment.query.filter_by(available_slot_id=data['available_slot_id'], is_active=True).first()

        # if appointment_by_other_user:
        #     response = jsonify({'message': 'This appointment is already booked by someone else.'})
        #     return response

        # new_appointment = Appointment(user_id=user_id,
        #                             available_slot_id=data['available_slot_id'],
        #                             is_visited=False,
        #                             is_active=True)

        # # Set the datetime value for the new appointment
        # new_appointment.datetime = available_slot.datetime

        # db.session.add(new_appointment)

        # # Mark the available slot as booked
        # available_slot.is_booked = True

      
        # db.session.commit()

        # response = jsonify({'message': 'Appointment added successfully.'})
        # return response


    