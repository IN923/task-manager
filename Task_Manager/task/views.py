from django.shortcuts import render
from django.views import View
from .models import Task
from django.http import JsonResponse
# Create your views here.

class All_Task(View):
    def get(self,request,*args,**kwargs):
        tasks = Task.objects.all()
        all_tasks = JsonResponse(tasks,safe=False)
        return all_tasks