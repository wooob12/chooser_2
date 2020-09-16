from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from main.models import User, Debate, Comment_debate, Vote
# Create your views here.


def debate_index(request):
    all_debate = Debate.objects.all()
    debates = Debate.objects
    debate_list = Debate.objects.all()
    paginator = Paginator(debate_list, 1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'debate_index.html', {'all_debate':all_debate, 'debates':debates, 'posts':posts})


def debate_create(request):
    if request.method == "POST":
        filled_form = DebateForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.save()
            return redirect('debate_index')
    debate_form = DebateForm()
    return render(request, 'debate_create.html', {'debate_form':debate_form})

def debate_detail(request):
    return render(request, 'debate_detail.html')

def debate_create_comment(request, debate_id):
    debate_comment_form = CommentForm(request.POST)
    if debate_comment_form.is_valid():
        temp_form = debate_comment_form.save(commit=False)
        temp_form.com_deb_member_id = request.user
        temp_form.com_deb_debate_id = debate.objects.get(pk=debate_id)
        temp_form.debate = Debate.objects.get(pk=debate_id)
        temp_form.save()
        return redirect('debate_detail', debate_id)
    else: 
        return redirect('debate_detail', debate_id)

def debate_delete_comment(request, debate_id, com_deb_id):
    debate_my_comment = Comment_debate.objects.get(pk=com_deb_id)
    if request.user == debate_my_comment.com_deb_member_id:
        debate_my_comment.delete()
        return redirect('debate_detail', debate_id)

    else:
        raise PermissionDenied