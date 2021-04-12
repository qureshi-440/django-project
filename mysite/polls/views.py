from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html' , {'name':'Farhan'})

def add(request):
    val1 = int(request.POST['Num1'])
    val2 = int(request.POST['Num2'])
    res = val1 + val2
    return render(request,'index.html',{'name':res})