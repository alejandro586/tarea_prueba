import requests
from django.conf import settings

BASE_URL = "https://services.leadconnectorhq.com"

def create_appointment(data):
    url = f"{BASE_URL}/calendars/events/appointments"
    headers = {
        "Authorization": f"Bearer {settings.GHL_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def list_appointments(calendar_id):
    url = f"{BASE_URL}/calendars/events/appointments?calendarId={calendar_id}"
    headers = {
        "Authorization": f"Bearer {settings.GHL_ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
