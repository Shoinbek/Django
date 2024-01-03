# This url is in the app level and I had to create it. 
from django.urls import path
from . import views # to connect to the views folder which is within the app folder

urlpatterns = [
    path('', views.homepage),
    path('home',views.home),
    path('dishes/<str:dish>', views.menuitems),
    path('drinks/<str:drink>', views.drinks)
]