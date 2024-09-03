from django.urls import path
from m_lab.apps import MLabConfig
from . import views
from django.views.decorators.cache import cache_page, never_cache

app_name = MLabConfig.name
urlpatterns = [
    path('', cache_page(60)(views.Main.as_view()), name='main'),
]
