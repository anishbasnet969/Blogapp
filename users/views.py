from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Create your views here.
def user_registration_view(request):
    form = RegistrationForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        messages.success(request, f'Your account has been created!Now,you can log in.')
        return redirect('login')

    return render(request,'users/register.html', {'form':form})    

@login_required
def profile_view(request):
    return render(request,'users/profile.html')
    

    
