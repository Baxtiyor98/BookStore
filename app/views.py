from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import  authenticate , login , logout
from django.http import HttpResponse , JsonResponse
import  json
def index(request):
    categ = Category.objects.all()
    return render(request,'index.html',{'categories':categ})
def category(request):
    categ = Category.objects.all()
    return render(request,'categories.html',{'categories':categ})
def category_in(request,id):
    categ = Category.objects.get(id=id)
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
    return render(request, 'product_lesson.html', context)
def inside_lesson(request,id,pr):
    first_item = Inside_Products_File.objects.filter(product_id = pr).order_by('id')[0]
    les = Products.objects.get(id=1)
    lesson = Inside_Products_File.objects.get(id=id)
    print(first_item.id,lesson)
    if first_item.name == lesson.name or request.user.is_authenticated:
        return render(request, 'inside_lesson.html', {'lesson':lesson,
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
def dashboard(request):
    c = Category.objects.all()
    if request.method == 'POST':
        print('Post')
        addc = Add_category(request.POST,request.FILES)
        if addc.is_valid():
            print('is valid.....')
            name = request.POST.get('name')
            image = request.FILES.get('image')
            description = request.POST.get('description')
            add_categ = Category(name=name,image=image,description=description)
            add_categ.save()
            return redirect('dashboard')
        else:
            return HttpResponse("Error")
    return render(request, 'dashboard/dashboard.html', {'categories':c})
def pr_category(request):
    data = json.loads(request.body)
    lesson = Products.objects.filter(category_id = data['category'])
    print(lesson)
    context = []
    for c in lesson:
        d = {
            'name':c.name,
            'image':c.imageURL,
            'description':c.description
        }
        context.append(d)
    return JsonResponse({'data':context})
def save(request):
    data = json.loads(request.body)
    print(data)
    return JsonResponse({'status':'ok'})