from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User 
# from django.contrib import messages
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == "POST":
        username_1 = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username_1,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('./travell')
        else :
            messages.info(request,'Username or password Incorrect')
            return redirect('login')
    else :
        return render(request,'travell/login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        conf_password = request.POST['password1']
        email_id = request.POST['email_id']

        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already exists")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request,'Email Already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,email = email_id,password=password,first_name=first_name,last_name=last_name)
                user.save()
                print("User Created")
            
        else :
            messages.info(request,"Password's doesn't match")
            return redirect('register')
        return redirect('../')
    else:
        return render(request,'travell/register.html')


# logout 
def logout(request):
    auth.logout(request)
    return redirect("../")