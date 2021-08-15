import django.views.generic
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoform
from  django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('detailv',kwargs={'pk':self.object.id})
class taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url= reverse_lazy('cbvlist')

def home(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})
def delete(request,id):
    task2 = Task.objects.get(id=id)
    if request.method=='POST':
        task2.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task=Task.objects.get(id=id)
    form=todoform(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})