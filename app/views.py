from django.shortcuts import render, redirect
from .models import *
from .forms import Login,Register
from django.contrib.auth import  authenticate , login , logout

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

def inside_lesson(request,id,tr):
    print(request.user)
    if tr==1 or request.user.is_authenticated:
        print('id keldi.....',id)
        les = Products.objects.get(id=id)
        lesson = Inside_Products_File.objects.filter(id=id)
        print(lesson)
        return render(request, 'inside_lesson.html', {'inside_lesson':lesson,
                                                  'lesson_name':les})
    else:
        return redirect(log_in)

def log_in(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request=request , username = username , password = password)
            if user:
                login(request, user)
                return redirect(index)
    return render(request, 'login.html',{})
def log_out(request):
    logout(request)
    return redirect(log_in)

def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request=request , username=username , password=password)
            if user:
                login(request , user)
                return redirect(index)
    return render(request , 'register.html' ,{})