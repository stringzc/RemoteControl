from django.urls import re_path
from Monitor.consumers.index import ControlConsumer

websocket_urlpatterns = [
    re_path(r'ws/ControlConsumer/(?P<device_id>\w+)/$', ControlConsumer.as_asgi()),
]