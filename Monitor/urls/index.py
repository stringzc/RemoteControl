from django.urls import path, include

from Monitor.views.index import index

urlpatterns = [
    path("", index, name="index"),
    path("wx/", include("Monitor.urls.wx.index")),
    path("web/", include("Monitor.urls.web.index"))
]
