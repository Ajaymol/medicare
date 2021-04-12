from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Category, Doctor


# Create your views here.
def demo(request):
    return HttpResponse('WELCOME')


def allDoctCat(request, c_slug=None):
    c_page = None
    doctors = None
    if c_slug!= None:
        c_page = get_object_or_404(Category, slug=c_slug)
        doctors = Doctor.objects.filter(category=c_page, available=True)
    else:
        doctors = Doctor.objects.all().filter(available=True)
    return render(request, 'category.html', {'category': c_page, 'doctors': doctors})


def DoctorDetail(request,c_slug, doctor_slug):
    try:
       doctor = Doctor.objects.get(category__slug=c_slug, slug=doctor_slug)

    except Doctor.DoesNotExist:
        raise Http404("page not found")

    return render(request, 'doctor.html', {'doctor': doctor})
def doctor_name(request):
    doc=Doctor.objects.all()
    return render(request,'doctor.html',{'doc':doc})
