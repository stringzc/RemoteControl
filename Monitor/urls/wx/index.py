from django.urls import path, include

urlpatterns = [
    path("Login/", include("Monitor.urls.wx.Login.index")),
    # path("web/", include("Monitor.urls.web.index"))
]
