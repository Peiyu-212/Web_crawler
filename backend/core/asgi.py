import os  # noqa

import django  # noqa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.news.urls import socket_urlpatterns  # noqa
from channels.auth import AuthMiddlewareStack  # noqa
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa

from django.core.asgi import get_asgi_application  # noqa

application = ProtocolTypeRouter({
    # http request
    "http": get_asgi_application(),
    # websocket request
    "websocket": AuthMiddlewareStack(
        URLRouter(
            socket_urlpatterns
        )
    ),
})
