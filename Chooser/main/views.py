from django.shortcuts import render, redirect
from main.forms import JoinForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Login failed. Try again.')
    else:
        form = LoginForm()
        return render(request, 'login.html')

def join(request):
    join_form = JoinForm()
    if request.method == "POST":
        filled_form = JoinForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('home')
    return render(request, 'join.html', {'join_form': join_form})

def mypage(request):
    return render(request, 'mypage.html')

def signout(request):
    logout(request)
    return redirect('home')