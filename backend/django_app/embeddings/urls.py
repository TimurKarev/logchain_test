from django.urls import path
from .rests import EmbeddingsRest

urlpatterns = [
    path('', EmbeddingsRest.as_view()),
    ]