import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment

@csrf_exempt
def ghl_webhook(request):
    if request.method == "POST":
        try:
            payload = json.loads(request.body.decode("utf-8"))

            # Extraer datos
            appointment_id = payload.get("id")
            calendar_id = payload.get("calendarId")
            start_time = payload.get("startTime")
            end_time = payload.get("endTime")
            status = payload.get("status", "confirmed")

            # Guardar en DB
            Appointment.objects.update_or_create(
                appointment_id=appointment_id,
                defaults={
                    "calendar_id": calendar_id,
                    "start_time": start_time,
                    "end_time": end_time,
                    "status": status,
                },
            )

            print("Webhook recibido:", payload)
            return JsonResponse({"status": "ok"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)
