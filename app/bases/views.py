from django.shortcuts import render
from django.views import generic


# create view
class Home(generic.TemplateView):
    template_name = 'bases/home.html'

