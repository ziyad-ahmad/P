from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout,get_user_model
from django .contrib import messages
user = get_user_model()

def index(request):
    return render(request, 'authentication/index.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request,username=username,password=password)
        if auth_user is not None:
            auth_login(request,auth_user)
            return redirect(index)
    return render(request,'authentication/login.html')
def logout(request):
    auth_logout(request)
    return redirect('index')
def signup(request):
    if request.method == 'post':
            
        first_name=request.Post['first_name']
        last_name=request.Post.gat['last_name','']
        username=request.Post['username']
        email=request.Post['email']
        password=request.Post['password']
        try:
            messages.info(request, 'User can try to create account')
            user = user.objects.create_user(username=username,email=email,password=password,firs_tname=first_name,last_tname=last_name)
            auth_login(request,user)
            return redirect('index')
        except Exception as e:
            print('Error Creating User',e)
            messages.error(request,'Error created my Username or email my be existed')
        return render(request, 'authentication/signup.html')

