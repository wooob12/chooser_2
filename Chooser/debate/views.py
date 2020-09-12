from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.paginator import Paginator
from main.models import Member, Debate, Comment_debate, Vote
# Create your views here.

def debate_index(request):
    return render(request, 'debate_index.html')

def debate_create(request):
    return render(request, 'debate_create.html')

def debate_detail(request):
    return render(request, 'debate_detail.html')