from django.urls import path
from . import consumers



ws_URLPatterns=[
    path('/ws/sc/', consumers.SyncChatConsumer.as_asgi()),
    # path('/ws/ac/', consumers.AsyncChatConsumer.as_asgi()),
    
]