from django.urls import path
from .rests import some_view

urlpatterns = [
    path('', some_view),
    ]