from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages #! for flash messages

from . forms import MyUserCreationForm, LoginForm

from . models import User

# Create your views here.

def register_view(request):

    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Hey {username} your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])

            login(request, new_user)
            return redirect('core:index')
        else:
            messages.error(request, 'An error occurred during Registration')

    context = {'form': form}
    return render(request, 'userAuth/register.html', context)   


def login_view(request):

    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in :)')
        return redirect('core:index')


    if request.method == 'POST':

        # form = LoginForm(request.POST)
    
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('core:index')
        else:
            messages.error(request,'username or password is incorrect')
    
    context = {}
    return render(request, 'userAuth/login.html', context)


def logout_view(request):

    logout(request)

    messages.success(request, "Logout success")

    return redirect('userAuth:login')

    