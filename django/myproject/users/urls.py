from django.urls import path
# pyrefly: ignore[missing-import]
from . import views

urlpatterns = [
    path('home/', views.home),  # Empty quotes mean the root/homepage URL
]
