from django.urls import path
from .import views
app_name='feedback'
urlpatterns = [
    path('feedback',views.feedback, name='feedback'),
    path('register', views.register, name='register'),
    path('appointment', views.appointment, name='appointment'),
    ]