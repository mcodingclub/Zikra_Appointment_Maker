from app.common.models import AvailableSlot, Appointment
from datetime import datetime , timedelta
from threading import Thread
from app import db
from flask_restful import Resource
from time import sleep
from app import app
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

class CancelExpiredAppointmentView(Resource):

    @staticmethod
    def cancel_expired_appointments():
       
        with app.app_context():
            current_date = datetime.now().date()

            expired_appointments = Appointment.query.filter(
                Appointment.is_active == True,
                Appointment.is_visited == False,
                Appointment.available_slot_id == AvailableSlot.id,
                AvailableSlot.datetime <= current_date
            ).all()

            for appointment in expired_appointments:
                appointment.is_active = False
                appointment.admin_feedback = "Appointment automatically canceled due to user no-show."
                available_slot = AvailableSlot.query.get(appointment.available_slot_id)
                available_slot.is_cancelled = True
                db.session.commit()

    scheduler.add_job(cancel_expired_appointments, 'interval', hours=23)


scheduler.start()
