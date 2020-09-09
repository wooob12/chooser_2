from django.shortcuts import render
from main.forms import MemberForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def join(request):
    if request.method == "POST":
        filled_form = MemberForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('home')

    member_form = MemberForm()
    return render(request, 'join.html', {'member_form':member_form})

def mypage(request):
    return render(request, 'mypage.html')