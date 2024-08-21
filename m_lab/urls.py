from django.urls import path
from m_lab.apps import MLabConfig
from . import views


app_name = MLabConfig.name
urlpatterns = [
    path('', views.Main.as_view(), name='main'),
]
