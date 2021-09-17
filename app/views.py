from django.shortcuts import render
from .models import *

def index(request):
    categ = Category.objects.all()
    return render(request,'index.html',{'categories':categ})
def category(request):
    categ = Category.objects.all()
    return render(request,'categories.html',{'categories':categ})
def category_in(request,id):
    print('id keldi.....',id)
    categ = Category.objects.filter(id=id)
    p = Products.objects.filter(category_id=id)
    return render(request, 'category_in.html', {'category_in':p,
                                                'category_in_2': categ,
                                                })

def cat_lesson(request,id):
    print('id keldi.....',id)
    les = Products.objects.get(id=id)
    lesson = Inside_Products_File.objects.filter(product_id=id)
    context = {
        'inside_lesson': lesson,
        'lesson_name': les
    }
    return render(request, 'cat_lesson.html', context)

def inside_lesson(request,id):
    if request.method=='GET':
        print('id keldi.....',id)
        les = Products.objects.get(id=id)
        lesson = Inside_Products_File.objects.filter(id=id)
        print(lesson)
        return render(request, 'inside_lesson.html', {'inside_lesson':lesson,
                                                  'lesson_name':les})

def log_in(request):
    return render(request, 'login.html',{})
