from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

def index(request):
    return render(request,'index.html')

def transfer(request, id):
    data = User.objects.get(id=id)
    
    return render(request,'transfer.html',{'data':data})

def banking(request):
    data = User.objects.all()
    return render(request,'banking.html',{'data':data})

def update(request,id):
    data = User.objects.all()
    form = User(request.POST)
    if request.method == "POST":
        amount1 = request.POST.get('amount1',)
        name = request.POST.get('name',)
        balance = request.POST.get('balance',)
    User.objects.filter(name=name).update(balance=sum(amount1,balance))
    redirect("/banking/")
    ok = True
    return render(request,'banking.html',{'data':data,'ok':ok})

def sum(amount1,balance):
    sum = int(amount1)+int(balance)
    return sum