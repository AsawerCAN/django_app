from .models import Profile
from .forms import ContactForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView, DetailView, DeleteView,UpdateView, TemplateView

# Class Base Views
#CURD
#CREATE
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model= Profile # model which we used
    form_class= ProfileForm # fields define
    template_name= 'matrimony/new_profile.html'
    success_url= reverse_lazy ('matrimony:profile_list')
    
# READ 
class ProfileListView(ListView):
    model= Profile # it creates profile_list
    template_name= 'matrimony/profile_list.html'
    
class ProfileDetailView(DetailView):
    model= Profile
    template_name= 'matrimony/profile_detail.html'


# UPDATE
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model= Profile # model which we used
    form_class= ProfileForm # fields define
    template_name= 'matrimony/new_profile.html'
    success_url= reverse_lazy ('matrimony:profile_list')


# DELETE 
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model= Profile # model which we used
    template_name= 'matrimony/confirm_delete.html'
    success_url= reverse_lazy ('matrimony:profile_list')

#FORM
class ContactView(FormView):
    template_name = 'matrimony/contact.html'
    form_class = ContactForm
    success_url= reverse_lazy ('matrimony:contact')
    
    def get_context_data(self, **kwargs): # if you want to show specific thing
        context = super().get_context_data(**kwargs) # this is for alredy added
        context["user"] = self.request.user # updated
        return context

#TEMPLATE
class ExampleTemplate(TemplateView):  # if u want to open one templete from one link
    template_name = 'matrimony/example.html'



