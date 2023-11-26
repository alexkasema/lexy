from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages #! for flash messages

from . forms import MyUserCreationForm

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
