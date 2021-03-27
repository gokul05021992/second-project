from django.shortcuts import render,redirect
from.form import employeeform
from.models import employee
from django.contrib import messages

# Create your views here.
def index(request):
    obj = employee.objects.all()
    return render(request,'crudapp/index.html',{'data': obj})
def create(request):
    if request.method =="POST":
        form = employeeform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'updated')
        else:
            return (request,'crudapp/create.html')
    else:
        form=employeeform
    context = {
        'form': form
    }
    return render(request,'crudapp/create.html',context)
def update(request,id):
    obj=employee.objects.get(id=id)
    if request.method =='POST':
        form = employeeform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request,'updated sucessfully')
        else:
            return redirect('crudapp/update.html')
    else:
        form = employeeform
    context = {
        'form': form
    }
    return render(request,'crudapp/update.html',context)
def delete(request,id):
    obj=employee.objects.get(id=id)
    obj.delete()
    return render(request,'crudapp/delete.html',{'gok':obj})
    return redirect('read')







