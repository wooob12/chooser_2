from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import PreferForm
# Cremainate yosur views herer
# Create your views here

def prefer_index(request):
    # # https://egg-money.tistory.com/111?category=811218 참조 (잘모름)
    # # 페이지네이션
    # prefers = Prefer.objects
    # prefer_list = Prefer.object.all()
    # paginator = Paginator(prefer_list, 20)
    # page = request.GET.get('prefer')
    # posts = paginator.get_page(page)

    # return render(request, 'prefer_index.html', {'prefers':prefers})
    return render(request, 'prefer_index.html')


def prefer_create(request):
    if request.method == "POST":
        filled_form = PreferForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('prefer_index')
    prefer_form = PreferForm()
    return render(request, 'prefer_create.html', {'prefer_form':prefer_form})





