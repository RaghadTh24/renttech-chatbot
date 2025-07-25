from django.urls import path
from .views import chatbot_home, chatbot_api

urlpatterns = [
    path('', chatbot_home, name='chatbot_home'),         # /chatbot/ -> صفحة HTML
    path('chat/', chatbot_api, name='chatbot_api'),      # /chatbot/chat/ -> API
]

