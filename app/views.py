from django.shortcuts import render
from .models import *

def index(request):
    categ = Category.objects.all()
    return render(request,'index.html',{'categories':categ})
def category(request):
    categ = Category.objects.all()
    return render(request,'categories.html',{'categories':categ})
def category_in(request,id):
    categ = Category.objects.filter(id=id)
    p = Products.objects.filter(category_id=id)
    return render(request, 'category_in.html', {'category_in':p,
                                                'category_in_2': categ,
                                                })







# API
#
# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import viewsets,status
# from .serializer import *
# class CategoryView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
# class ProductsView(viewsets.ModelViewSet):
#     queryset = Products.objects.all()
#     serializer_class = ProductsSerializer

