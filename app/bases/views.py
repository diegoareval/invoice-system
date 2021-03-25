from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# create view
class Home(LoginRequiredMixin, generic.TemplateView):
    login_url = '/admin/'
    template_name = 'bases/home.html'

