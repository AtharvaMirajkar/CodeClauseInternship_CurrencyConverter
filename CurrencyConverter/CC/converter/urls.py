from django.urls import path
from . import views


urlpatterns = [
    path('',  views.index, name="index"), 
    path('converter/', views.convert_currency, name="convert_currency"), 
]