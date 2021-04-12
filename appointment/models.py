from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=500)
    addr = models.CharField(max_length=500)
    email = models.EmailField()

    doctorname = models.CharField(max_length=500)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "Appointments"
    def __str__(self):
        return self.name
