from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm

# Create your views here.
def user_registration_view(request):
    form = RegistrationForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!')
        return redirect('home-page')

    return render(request,'users/register.html', {'form':form})    
    

    
