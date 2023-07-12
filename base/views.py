from django.shortcuts import render,redirect
from base.forms import SignUpForm
from django.contrib.auth import logout

def index(request):
    return render(request, 'base/base.html')

def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/home/')
    else:
        form = SignUpForm()

    return render(request, 'base/signup.html',{
        'form':form,
    })

def log_out(request):
    logout(request)

    return render(request, 'base/signup.html')
