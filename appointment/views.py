from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Appointment
from django.template import RequestContext
from django.template.context_processors import csrf

from .models import Appointment
from .forms import CreateAppointment

def create_appointment(request):

    if request.method == 'POST':
      f = CreateAppointment(request.POST)
      if f.is_valid():
        f.save()
        messages.add_message(request, messages.INFO, 'Appointment Submitted.')
        return redirect('/')
    else:
        f = CreateAppointment()
    return render(request, 'appointment.html', {'form': f})

    # if request.method == 'POST':
    #     name= request.POST['name']
    #     addr = request.POST['addr']
    #
    #     email = request.POST['email']
    #     doctorname = request.POST['doctorname']
    #     date = request.POST['date']
    #     appointment=Appointment(name=name,addr=addr,email=email,date=date,doctorname=doctorname)
    #     appointment.save()
    #     print("appoint saved")
    #     messages.info(request,'Appointment Successfully Booked')
    #     return redirect('/')
    # else:
    #     return render(request,'appointment.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contact(request):
    return render(request, 'contact.html')


