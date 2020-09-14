from django.shortcuts import render,redirect
from main.models import Mood
from .form import MoodForm


def mood(request):

    if request.method =="POST":
        filled_form=MoodForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.save()
            return redirect('month')
            

    mood_form=MoodForm()
    return render(request, 'mood.html',{"mood_form" : mood_form})

def month(request):

    # a = []    # 빈 리스트 생성
    # b = [ Mood.objects.all() ]

    # for i in range(5):
    #     line = []
    #     for j in range(7):
    #         print(b,end="")
    #     print()

    all_mood = Mood.objects.all()
    return render(request, 'month.html',{'all_mood':all_mood})
