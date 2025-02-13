from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic.edit import CreateView
from .forms import SignupForm

"""
Class-based views:

View = generic view
ListView = get a list of records
DetailView = get a single(detail) record
CreateView = create a new record
DeleteView = remove a record
UpdateView = modify an existing record
LoginView  = login
"""
# Create your views here.
class UserLoginView(LoginView):
    template_name = "users/login.html"
    
    def get_success_url(self):
        return reverse('home')

class SignUpView(CreateView):
    template_name = "users/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy('login')


def user_logout(request):
    logout(request)
    return redirect('login')



