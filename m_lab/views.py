from django.shortcuts import render
from django.views.generic import DetailView, ListView
from m_lab.models import Photo, Post



class Main(ListView):
    model = Post
    template_name = 'm_lab/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()
        return context
