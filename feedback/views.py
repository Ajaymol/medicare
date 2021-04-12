from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import FeedbackForm,CreateAppointment
from django.contrib import messages

# Create your views here.
def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('/')
    else:
        f = FeedbackForm()
    return render(request, 'feedback.html', {'form': f})
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']



        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        print("user created")
        return redirect('/')
    else:
        return render(request,'register.html')
def appointment(request):
    if request.method == 'POST':
      f = CreateAppointment(request.POST)
      if f.is_valid():
        f.save()
        messages.add_message(request, messages.INFO, 'Appointment Submitted.')
        return redirect('/')
    else:
        f = CreateAppointment()
    return render(request, 'appointment.html', {'form': f})

