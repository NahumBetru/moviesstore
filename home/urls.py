from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home.index'),  # root URL of the app
    path('about', views.about, name='home.about'),
]