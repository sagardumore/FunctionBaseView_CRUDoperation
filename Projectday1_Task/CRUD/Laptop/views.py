from django.shortcuts import render,redirect

# Create your views here.
from .forms import LaptopModelForm
from .models import Laptop

def AddLaptopView(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_laptop')
    template_name = 'Laptop/addlaptopform.html'
    context={'form':form}
    return render(request,template_name,context)

def ShowLaptopView(request):
    laptop=Laptop.objects.all()
    template_name= 'Laptop/showlaptopinfo.html'
    context={'laptop':laptop}
    return render(request,template_name,context)

def deleteLaptopView(request,i):
    laptop=Laptop.objects.get(id=i)
    if request.method == 'POST':
        laptop.delete()
        return redirect('show_laptop')
    template_name = 'Laptop/deletelaptop.html'
    context={'laptop':laptop}
    return render(request,template_name,context)

def updateLaptopView(request,i):
    laptop= Laptop.objects.get(id=i)
    form = LaptopModelForm(instance=laptop)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,instance=laptop)
        if form.is_valid():
            form.save()
            return  redirect('show_laptop')
    template_name= 'Laptop/addlaptopform.html'
    context={'form':form}
    return render(request,template_name,context)