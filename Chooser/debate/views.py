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
    paginator = Paginator(debate_list, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    turn render(request, 'debatse_index.html', {'all_debate':all_debate, 'debates':debates, 'posts':posts})

def my_debate_index(request):
    my_debate = Debate.objects.filter(debate_member_id=request.user)
    return render(request, 'debate_index.html', {'my_debate':my_debate})

@login_required(login_url='/login')
def debate_create(request):
    if request.method == "POST":
      filled_form = DebateForm(request.POST)'all_prefer':all_prefer, s, 'post':posts
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
pefer_commnt_form = CommentForm()
    re_prefer, 'prefercomment_form':_comment_form
def debate_delete_comment(request, debate_id, com_deb_id):
    debate_my_comment = Comment_debate.objects.get(pk=com_deb_id)
    if request.user == debate_my_comment.com_deb_member_id:
        debate_my_comment.delete()
        return redirect('debate_detail', debate_id)

    else:
        raise PermissionDenied=com_ser
        temp_form.com_pre_prefer_id = Prefer.object.gt(pk=pefer_id)        else:         return reirct('preer_detail',i)

df prefer_de_prefer

# 수정버튼# def prefer_update_comment(request, prefer_id, com_pre_id):#     prefer_my_comment = Comment_prefer.objects.get(pk=com_pre_id)
#     prefer_my_comment_form = CommentForm(instance=prefer_my_comment)
#     if request.method == "POST":
#         comment_updated_form = CommentForm(request.POST, instance=prefer_my_comment)
#         if comment_updated_form.is_valid():
#             comment_updated_form.request.user
#             comment_updated_form.save()
#             return redirect('prefer_detail', prefer_id)
#         return render(request, 'prefer_detail.html', {'prefer_my_comment_form':prefer_my_comment_form})

#     else:
#         raise PermissionDenied