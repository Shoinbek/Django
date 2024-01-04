from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage),
    path('dishes/<str:dish>', views.menuitems),
    path('drinks/<str:drink>', views.drinks),
    
]