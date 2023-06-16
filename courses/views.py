from datetime import date
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.cache import cache_page
from .models import Course,Category


def course_detail(request,slug):
    return render(request,'courses/detail.html',{'course':get_object_or_404(Course,slug=slug)})
    
    
def index(request):

    return render(request,'courses/index.html',{'categories':Category.objects.all(),"courses":Course.objects.all()})

def get_course_by_category(request,slug):
    return render(request, 'courses/index.html',{
        "courses": Course.objects.filter(category__slug=slug,isActive=True),
        "categories": Category.objects.all(),
        "selected":slug
    })
    
