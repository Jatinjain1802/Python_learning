
from django.urls import path
from . import views

urlpatterns = [
    path('display/', views.display_view),
    path('display_table/', views.display_table_view),

    path('',views.home_view),
    path('about/',views.about_view),
    path('contact/',views.contact_view),
]
