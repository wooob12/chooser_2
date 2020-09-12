from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from .forms import PreferForm
from main.models import User, Topic, Prefer, Comment_prefer
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

def prefer_detail(request, prefer_id):
    my_prefer = Prefer.objects.get(pk=prefer_id)
    return render(request, 'prefer_detail.html', {'my_prefer':my_prefer})
    # 왼쪽이 '내가 정해준 저장공간 이름', 오른쪽이 저장할 것의(객체) 이름

def prefer_delete(request, prefer_id):
    my_prefer = Prefer.objects.get(pk=jss_id)
    my_prefer.delete()
    return redirect('prefer_index')

def prefer_update(request, prefer_id):
    my_prefer = Prefer.objects.get(pk=prefer_id)
    prefer_form = PreferForm(instance=my_prefer)
    if request.method == "POST":
        updated_form = PreferForm(request.POST, instance_my_prefer)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('prefer_index')
    return render(request, 'prefer_create.html', {'prefer_form':prefer_form})


def prefer_create_comment(request, prefer_id):
    prefer_comment_form = CommentForm(request.POST)
    if prefer_comment_form.is_valid():
        temp_form = prefer_comment_form.save(commit=False)
        temp_form.author = request.user
        temp_form.prefer = Prefer.objects.get(pk=prefer_id)
        temp_form.save()
    return redirect('detail', prefer_id)





