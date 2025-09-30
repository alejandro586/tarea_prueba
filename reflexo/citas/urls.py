from django.urls import path
from . import views

urlpatterns = [
    path("webhooks/ghl/appointments/", views.ghl_webhook, name="ghl_webhook"),
]
