from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import Task
from django. views.generic import ListView
from django. views.generic import DetailView
from django. views.generic import UpdateView,DeleteView
# Create your views here.
class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'
class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ['name','priority','date']
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.pk})
class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')

def add (request):
    task1=None
    if request.method=="POST":
        name=request.POST.get('task','')
        priority = request.POST.get('priority', '')
        date= request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    task1 = Task.objects.all()
    return render(request,'home.html',{'task1':task1})
# def details(request):
#
#     return render(request,'detail.html',)
def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,task_id):
    task1 = Task.objects.get(id=task_id)
    f=TodoForm(request.POST or None, instance=task1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task1})