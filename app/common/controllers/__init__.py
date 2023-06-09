from flask_restful import Api
from flask import Blueprint
from app.common.controllers.admin_add_slot import AddSlotView 
from app.common.controllers.show_available_slot import GetAvailableSLotView
from app.common.controllers.book_appointment import BookAppointmentView
from app.common.controllers.user_see_appointment_number import GetAppointmentView
from app.common.controllers.user_cancel_appointment import CancelAppointmentView
from app.common.controllers.user_visited import VisitedAppointmentView
from app.common.controllers.admin_feedback import AdminFeedbackView
from app.common.controllers.Admin_can_view_booked_appointment import AdminCanShowBookedAppointmentView
from app.common.controllers.cancel_expired_appointment import CancelExpiredAppointmentView
from app.common.controllers.user_can_view_admin_feedback import ViewAdminFeedbackView


common_blueprint =Blueprint("common",__name__,url_prefix="/common")
api=Api(common_blueprint)

# http://127.0.0.1:5000/api/common/add_slot
api.add_resource(AddSlotView,"/add_slot/") 
api.add_resource(GetAvailableSLotView,"/show_slot/")
api.add_resource(BookAppointmentView,"/book_appoinment/") 
api.add_resource(GetAppointmentView,"/get_appointment/")
api.add_resource(CancelAppointmentView,"/cancel_appointment/")
api.add_resource(VisitedAppointmentView,"/visit_appointment/")
api.add_resource(AdminFeedbackView,"/admin_feedback/")
api.add_resource(AdminCanShowBookedAppointmentView,"/admin_booked_slot/")
api.add_resource(CancelExpiredAppointmentView,"/cancel_expired_appointment/")
api.add_resource(ViewAdminFeedbackView,"/user_view_feedback/")