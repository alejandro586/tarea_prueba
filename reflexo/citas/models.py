from django.db import models

class Appointment(models.Model):
    appointment_id = models.CharField(max_length=100, unique=True)
    calendar_id = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50, default="confirmed")

    def __str__(self):
        return f"{self.appointment_id} - {self.status}"
