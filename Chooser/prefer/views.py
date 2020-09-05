from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .forms import PreferForm
from .model import Prefer
# Create your views here

def prefer_create(request):
    if request.method == "POST":
        filled_form = PreferForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return redirect('prefer_index')
    prefer_form = PreferForm()
    return render(request, 'prefer_create.html', {'prefer_form':prefer_form})