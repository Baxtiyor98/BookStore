from .views import *
from django.urls import path

urlpatterns = [
    path('',index,name='index'),
    path('category/',category,name='category'),
    path('category_in/<int:id>',category_in,name='category_in'),
    path('cat_lesson/<int:id>',cat_lesson , name='cat_lesson'),
    path('inside_lesson/<int:id>',inside_lesson , name='inside_lesson'),
    path('log_in/', log_in, name='log_in'),
]