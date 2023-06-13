from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse


data={
    "mobil":"mobil programlama detayları",
    "masaüstü":"masaüstü programlama detayları",
    "gömülü-sistemler":"gömülü sistemler detayları",
    "django":"django detayları",
    ".net":".net detayları",
}

# Create your views here.
def index(request):
    return render(request,'courses/courses.html',{'data':data.keys})

def get_courses_by_cname(request,category):
    
    try:
        category_name = data[category]
        return render(request,'courses/courses.html',{
            'category':category,
            'category_name': category_name
        })
    except:
        return HttpResponseNotFound("böyle bir kategori bulunamadı")

def category_by_id(request,category_id):
    category_name = list(data.keys())
    if(category_id > len(category_name)):
        return HttpResponseNotFound("böyle bir kategori bulunamadı")
    
    redirect_url = reverse('category_by_id',args=[category_name[category_id-1]])


    return redirect(redirect_url)