from django.urls import path

from Monitor.views.wx.Plan.AddPlanInfoWithID import AddPlanInfoWithID
from Monitor.views.wx.Plan.CancelAct import CancelAct
from Monitor.views.wx.Plan.PlanAct import PlanAct
from Monitor.views.wx.Plan.SaveAutoRecords import SaveAutoRecords
from Monitor.views.wx.Plan.getAutoTimeWithPlanID import getAutoTimeWithPlanID
from Monitor.views.wx.Plan.getModelInfoWithPlanID import getModelInfoWithPlanID
from Monitor.views.wx.Plan.getPlanInfoWithID import getPlanInfoWithID

urlpatterns = [
    path("getPlanInfoWithID/", getPlanInfoWithID.as_view()),  # getPhoneNumber
    path("getModelInfoWithPlanID/", getModelInfoWithPlanID.as_view()),  # savePhoneNumber
    path("getAutoTimeWithPlanID/", getAutoTimeWithPlanID.as_view()),
    path("AddPlanInfoWithID/", AddPlanInfoWithID.as_view()),  # CancelAct
    path("CancelAct/", CancelAct.as_view()),
    path("PlanAct/", PlanAct.as_view()),  # saveAutoRecords
    path("SaveAutoRecords/", SaveAutoRecords.as_view())
]
