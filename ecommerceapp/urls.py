from django.urls import path
from .import views
app_name='ecommerceapp'

urlpatterns=[
    path('',views.allDoctCat,name='allDoctCat'),
    path('<slug:c_slug>/',views.allDoctCat,name='doctors by category'),
    path('<slug:c_slug>/<slug:doctor_slug>/',views.DoctorDetail,name='doctorsDetails'),
    path('<slug:c_slug>',views.DoctorDetail,name='doctorsDetail'),
    path('doctor',views.doctor_name,name='doctors'),
]