from django.shortcuts import get_object_or_404, redirect, render
from .models import Course,Category
from django.core.paginator import Paginator


def course_detail(request,slug):
    return render(request,'courses/detail.html',{'course':get_object_or_404(Course,slug=slug)})

def index(request):
    paginator = Paginator(Course.objects.filter(isActive=True),3)
    page = request.GET.get('page',1)
    return render(request,'courses/index.html',{'categories':Category.objects.all(),"courses":paginator.get_page(page),"paginator":[i for i in range(paginator.count)]})

def get_course_by_category(request,slug):
    paginator = Paginator(Course.objects.filter(categories__slug=slug,isActive=True),3)
    page = request.GET.get('page',1)
    return render(request, 'courses/index.html',{
        "courses": paginator.page(page),
        "categories": Category.objects.all(),
        "selected":slug,
    })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True,title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        redirect("/kurslar")
    paginator = Paginator(kurslar,3)

    return render(request,"courses/index.html",{
        "categories":kategoriler,
        "courses":paginator
    })

def create(request):
    


    return render('courses/create.html')