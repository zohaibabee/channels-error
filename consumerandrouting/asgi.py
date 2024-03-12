"""
ASGI config for consumerandrouting project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from app.consumers import SyncChatConsumer
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import app.routing
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'consumerandrouting.settings')

application = ProtocolTypeRouter({
    "http":get_asgi_application(),
   "wesocket": URLRouter([
      
    path('ws/sc/', SyncChatConsumer.as_asgi()),
])
})