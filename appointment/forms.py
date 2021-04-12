from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model


from .models import Appointment


class CreateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'