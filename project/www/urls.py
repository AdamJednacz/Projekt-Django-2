from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    # Dla widoku index
    path('index2/', views.index2, name='index2'),  # Dla widoku index2
    path('accept_offer/', views.accept_offer, name='accept_offer'), 
]
