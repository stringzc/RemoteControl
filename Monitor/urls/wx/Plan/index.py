from django.urls import path

from Monitor.views.wx.Plan.getAutoTimeWithPlanID import getAutoTimeWithPlanID
from Monitor.views.wx.Plan.getModelInfoWithPlanID import getModelInfoWithPlanID
from Monitor.views.wx.Plan.getPlanInfoWithID import getPlanInfoWithID

urlpatterns = [
    path("getPlanInfoWithID/", getPlanInfoWithID, name="wx_Plan_getPlanInfoWithID"),  # getPhoneNumber
    path("getModelInfoWithPlanID/", getModelInfoWithPlanID, name="wx_Plan_getModelInfoWithPlanID"),  # savePhoneNumber
    path("getAutoTimeWithPlanID/", getAutoTimeWithPlanID, name="wx_Plan_getAutoTimeWithPlanID"),
]
