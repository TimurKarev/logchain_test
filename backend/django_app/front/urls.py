from django.urls import path
from .views.document_loader_view import DocumentLoaderView

urlpatterns = [
    path('', DocumentLoaderView.as_view()),
    ]