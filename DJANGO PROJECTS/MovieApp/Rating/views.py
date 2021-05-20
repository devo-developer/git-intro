from django.shortcuts import redirect, render
from django.http import HttpResponse

from django import forms
from Rating.forms import registerForm
from .models import User
from hashlib import sha256

# Create your views here.


def index(request):
    return HttpResponse("<h1>Welcome to Movie Review App</h1>")


def about(request):
    return HttpResponse("<h1>This is about Page</h1>")


def register(request):
    form = registerForm()
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('Last_name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            password = sha256(pass2.encode()).hexdigest()
            User(first_name=firstname, Last_name=lastname, gender=gender,
                 date_of_birth=date_of_birth, email=email, phone=phone, password=password).save()
        return redirect('/MovieApp/register')

    else:
        form = registerForm()
        return render(request, 'registration.html', {'form': form})


def login(request):
    return render(request, 'login.html')


def movies(request):
    return render(request, 'ratin/movies.html')


def details(request):
    return render(request, 'ratin/details.html')
