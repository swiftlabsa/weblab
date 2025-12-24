from django.urls import path, include
from . import views

urlpatterns = [
    path('5157da30-3fba-40f3-986d-8b808b4804b1', views.whatsapp_webhook, name='webhook')
]
