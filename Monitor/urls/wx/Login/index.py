from django.urls import path, include

from Monitor.views.wx.Login.getPhoneNumber import getPhoneNumber
from Monitor.views.wx.Login.getUid import getUid
from Monitor.views.wx.Login.savePhoneNumber import savePhoneNumber

urlpatterns = [
    path("getUid/", getUid, name="wx_Login_getUid"),  # getPhoneNumber
    path("getPhoneNumber/", getPhoneNumber, name="wx_Login_getPhoneNumber"),  # savePhoneNumber
    path("savePhoneNumber/", savePhoneNumber, name="wx_Login_savePhoneNumber")
    # path("web/", include("Monitor.urls.web.index"))
]
