from django.urls import path, include

from Monitor.views.wx.Login.UserProfileView import UserProfileView
from Monitor.views.wx.Login.getPhoneNumber import getPhoneNumber
from Monitor.views.wx.Login.getUid import getUid
from Monitor.views.wx.Login.savePhoneNumber import savePhoneNumber

urlpatterns = [
    path("getUid/", getUid.as_view()),  # getPhoneNumber
    path("getPhoneNumber/", getPhoneNumber.as_view()),  # savePhoneNumber
    path("savePhoneNumber/", savePhoneNumber.as_view()),
    path("UserProfileView/", UserProfileView.as_view())
    # path("web/", include("Monitor.urls.web.index"))
]
