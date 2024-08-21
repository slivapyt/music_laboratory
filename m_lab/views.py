from django.shortcuts import render
from django.views.generic import DetailView, ListView
from m_lab.models import Post



class Main(ListView):
    model = Post
    template_name = 'm_lab/index.html'
