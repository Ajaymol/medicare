from django import forms
from .models import Feedback,Appointment


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
class CreateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'