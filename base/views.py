from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from base.forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, 'base.html')

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

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        # Authenticate the user
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            # Redirect to the desired URL after successful login
            return redirect('video:videos')  # Replace 'base:success' with the name of your success view
        else:
            form.add_error(None, 'Invalid username or password.')

        return super().form_invalid(form)


def log_out(request):
    logout(request)

    return redirect('video:videos')
