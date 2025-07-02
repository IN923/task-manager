from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views import View
from .models import Task
from django.http import JsonResponse
# Create your views here.

class All_Task(View):
    def get(self,request,*args,**kwargs):
        tasks = Task.objects.all().values()
        all_tasks = list(tasks)
        return JsonResponse(all_tasks,safe=False)
    
class Create_task(CreateView):
    model = Task
    fields = ['name']
    template_name = 'task/task_create_form.html'
    success_url = 'create'
