from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('category/',category,name='category'),
    path('category_in/<int:id>',category_in,name='category_in')
]