from django.urls import path, include

urlpatterns = [
    path("Login/", include("Monitor.urls.wx.Login.index")),
    path("Plan/", include("Monitor.urls.wx.Plan.index")),
    # path("web/", include("Monitor.urls.web.index"))
]
