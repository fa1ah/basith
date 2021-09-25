from django.shortcuts import render


# Create your views here.
from BloodBank.models import Bloody


def home(request):
    return render(request, 'home.html')


def add(request):
    blood1 = Bloody()
    blood1.name = request.POST['firstname']
    blood1.contact = request.POST['num']
    blood1.blood = request.POST['blood']
    name1 = [blood1]
    return render(request, 'result.html', {'name': name1})
