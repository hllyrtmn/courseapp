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

def get_category_by_id(request,category_id):
    
    # return HttpResponse(filtered_data)
    return render(request, 'courses/partials/_courses.html')
    
