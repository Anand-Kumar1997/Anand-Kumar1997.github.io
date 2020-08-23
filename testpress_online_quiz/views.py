from django.shortcuts import render
from testpress_online_quiz.models import Exam

def onlinequiz(request):
    results=Exam.objects.all()
    return render(request,'main.html',{"Exam":results})

def quiz(request):
    return render(request,'index.html')


