from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .forms import destination_form

# Create your views here.

def home(request):
    dests = Destination.objects.all()
    return render(request, 'travell/index.html',{'dests':dests} )

def site_upload(request):
    uploaded = False
    dest = destination_form()
    if request.method == "POST":
        dest = destination_form(request.POST,request.FILES)
        if dest.is_valid():
            dest.save()
            uploaded = True
            return redirect("./")
    return render(request,"travell/upload.html",{'form':dest})
