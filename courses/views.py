from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse


data={
    "mobil":"mobil programlama detayları",
    "masaüstü":"masaüstü programlama detayları",
    "gömülü-sistemler":"gömülü sistemler detayları",
}


# Create your views here.
def courses(request):
    return HttpResponse("kurslar sayfası")
def details(request):
    return HttpResponse("detaylar sayfası")
# def programming(request):
#     return HttpResponse("programlama sayfası")
# def mobile_app(request):
#     return HttpResponse("mobil uygulama sayfası")
def get_courses_by_cname(request,category):
    
    try:
        category_text = data[category]
        return HttpResponse(f'{category} sayfası')
    except:
        return HttpResponseNotFound("böyle bir kategori bulunamadı")

def category_by_id(request,category_id):
    category_name = list(data.keys())
    if(category_id > len(category_name)):
        return HttpResponseNotFound("böyle bir kategori bulunamadı")
    
    redirect_url = reverse('category_by_id',args=[category_name[category_id-1]])

    return redirect(redirect_url)