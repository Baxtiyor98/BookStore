from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('category/',category,name='category'),
    path('category_in/<int:id>',category_in,name='category_in'),
    path('cat_lesson/<int:id>',cat_lesson , name='cat_lesson'),
    path('inside_lesson/<int:id>/<int:pr>',inside_lesson , name='inside_lesson'),
    path('register/' , register, name='register'),
    path('log_in/', log_in, name='log_in'),
    path('log_out/' , log_out , name='log_out')
]