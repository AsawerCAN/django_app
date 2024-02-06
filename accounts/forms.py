from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django import forms

class RegistrationForm(UserCreationForm): #inherit from UserCreationForm
    
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, widget=forms.RadioSelect)
    
    class Meta: # call existing model in that model
        model = CustomUser
        fields= ['username', 'email', 'gender','password1', 'password2'] #already exists thes fields in usercreationform model
        
