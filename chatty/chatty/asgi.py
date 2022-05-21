"""
ASGI config for chatty project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatty.settings')

# application = get_asgi_application()



import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

# import chat.routing

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatty.settings')

# django_asgi_app = get_asgi_application()

django.setup()

# application = get_asgi_application()
# from chat.consumers import ChatConsumer
import chat.routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})

