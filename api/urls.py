from django.urls import path
from . import views

urlpatterns = [
    path('shorten-url', views.shorten_url)
]