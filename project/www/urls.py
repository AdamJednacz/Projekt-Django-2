from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('index2/', views.index2, name='index2'),  
    path('accept_offer/', views.accept_offer, name='accept_offer') ,
    path('like/', views.like, name='like'),
    path('unlike/', views.unlike, name='unlike'),
]
