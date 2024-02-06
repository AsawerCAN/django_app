from django import forms
from .models import *

from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

def my_email_validator(email):
    if email.split('@')[1].split('.')[0].lower() == 'hotmail':
        raise ValidationError("Email Not Acceptable")


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator(),my_email_validator])
    verify_email = forms.CharField()
    message=forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get('name')
        cleaned_data['email'] = cleaned_data.get('email').lower()
        cleaned_data['verify_email'] = cleaned_data.get('verify_email').lower()
        message = cleaned_data.get('message')

        if cleaned_data.get('email') != cleaned_data.get('verify_email'):
            raise forms.ValidationError("Email Mismatch")
        
        return cleaned_data
    
class ProfileForm(forms.ModelForm):
    class Meta: # call existing model in that model
        model= Profile
        fields= "__all__"  # ad all fields from Profile model
        #fields= ['name', 'age', 'gender'] #ad specific fields
         #exclude = ['name', 'age', 'gender']




































# from django import forms

# from django.core.validators import EmailValidator
# from django.core.exceptions import ValidationError

# def my_email_validator(email): #custom email validator
#     if email.split('@')[1].split('.')[0].lower() == 'hotmail': #email.split('@') split into two parts before[0] and after[1] @. [1](which is gmail.com).split('.')(split into two parts bfore[0] after[1].)[0]([0]is 'gmail' and 'com'is[1])
#         raise ValidationError("Email Not Acceptable")


# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=100)
#     email = forms.CharField(validators=[EmailValidator(),my_email_validator])
#     verify_email = forms.CharField()
#     message=forms.CharField(widget=forms.Textarea)

#     def clean(self): # this clean function itself called u dnt need to cal beacause in ContactView (if form.is_valid():) this will call that clean function
#         cleaned_data = super().clean() # default method you need to use in clean always. super() is to run default clean method

#         name = cleaned_data.get('name')

#     # Lowercasing email and verify_email if they exist
#         email = cleaned_data.get('email')
#         if email:
#             cleaned_data['email'] = email.lower()

#         verify_email = cleaned_data.get('verify_email')
#         if verify_email:
#             cleaned_data['verify_email'] = verify_email.lower()

#         message = cleaned_data.get('message')

#     # Checking if email and verify_email match
#         if cleaned_data.get('email') != cleaned_data.get('verify_email'):
#             raise forms.ValidationError("Email Mismatch")
    
        
#         return cleaned_data
    

        


    

        

    