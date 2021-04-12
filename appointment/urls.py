from django.urls import path
from .import views
app_name='appointment'
urlpatterns=[
   path('appointment',views.create_appointment,name='appointment'),
   path('aboutus',views.aboutus,name='aboutus'),
   path('contact', views.contact, name='contact'),

]