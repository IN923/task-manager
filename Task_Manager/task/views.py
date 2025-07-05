from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views import View
from .models import Task
from django.http import JsonResponse
import json
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'task/index.html')

class All_Task(View):
    def get(self,request,*args,**kwargs):
        tasks = Task.objects.all().values()
        all_tasks = list(tasks)
        return JsonResponse(all_tasks,safe=False)
    
class CreateTask(CreateView):

    def post(self,request,*args,**kwargs):
        # self.object = None
        # return super().post(request,*args,**kwargs)
        body_unicode = request.body.decode('utf-8')
        task_name = json.loads(body_unicode)
        if len(task_name)==0:
            return JsonResponse({'error':'Task is Empty'},status=400)
        return JsonResponse(f'{task_name}',safe=False)
    
class UpdateTask():
    pass