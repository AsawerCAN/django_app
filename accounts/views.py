from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout # authenticate chk if user ad valid data which already ad
from .forms import RegistrationForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

# Create your views here.

def RegisterView(request):
    if request.method=='POST':
        form= RegistrationForm(request.POST) #default register form redirect to admin page thats why temples are created
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form= RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})       

def LoginView(request):   # Session based authentication used here for login logout, wherever Token based authentication is used in APIs
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST) # vaiable name specify for non possitional variable
        
        if form.is_valid():
            user= form.get_user()
            login (request, user)   # login start session of certain user #Aswoo pas: JG&%98tryu
            return redirect('matrimony:profile_list')
    else:
        form= AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form}) 

def LogoutView(request):
    logout(request)  # cookies store in client side browser. for exp user selec any lang to saw website next time login automaticall used that language
    if request.method == "POST":
        return JsonResponse({'success': True})
    return redirect('accounts:login')

def DeleteView(request):
    request.user.delete() # delete the user which requests
    messages.Success(request, 'Your account has been deleted successfully') # builin module to show message
    redirect('accounts:login')