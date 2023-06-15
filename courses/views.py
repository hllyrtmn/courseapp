from datetime import date
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.cache import cache_page
from .models import Course,Category


# data={
#     "mobil":"mobil programlama detayları",
#     "masaüstü":"masaüstü programlama detayları",
#     "gömülü-sistemler":"gömülü sistemler detayları",
#     "django":"django detayları",
#     ".net":".net detayları",
# }

#  db = {
#     "courses":[
#         {
#             "id":1,
#             "category_id":1,
#             "title":"python kursu",
#             "description":"python kurs açıklaması",
#             "image_url":"1.png",
#             "slug":"python-kursu",
#             "date":date(2023,10,10),
#             "is_active":True,
#             "is_update":True
#         },
#         {
#             "id":2,
#             "category_id":2,
#             "title":"angular kursu",
#             "description":"angular kurs açıklaması",
#             "image_url":"2.png",
#             "slug":"angular-kursu",
#             "date":date(2023,8,10),
#             "is_active":True,
#             "is_update":False
#         },
#         {
#             "id":3,
#             "category_id":1,
#             "title":"c# kursu",
#             "description":"c# kurs açıklaması",
#             "image_url":"3.png",
#             "slug":"c-sharp-kursu",
#             "date":date(2023,3,10),
#             "is_active":True,
#             "is_update":True
            
#         },
#         {
#             "id":4,
#             "category_id":1,
#             "title":"java kursu",
#             "description":"java kurs açıklaması",
#             "image_url":"4.png",
#             "slug":"java-kursu",
#             "date":date(2023,1,10),
#             "is_active":True,
#             "is_update":True
#         },
#         {
#             "id":5,
#             "category_id":3,
#             "title":"matlab kursu",
#             "description":"matlab kurs açıklaması",
#             "image_url":"5.png",
#             "slug":"matlab-kursu",
#             "date":date(2023,12,10),
#             "is_active":True,
#             "is_update":True
            
#         },
#         {
#             "id":6,
#             "category_id":4,
#             "title":"mobil excel kursu",
#             "description":"mobil excel kurs açıklaması",
#             "image_url":"6.png",
#             "slug":"mobil-excel-kursu",
#             "date":date(2023,12,5),
#             "is_active":True,
#             "is_update":False
#         },
#     ],
#     "categories":[
#         {"name":"Yazılım Dilleri","slug":"yazilim-dilleri","id":1},
#         {"name":"Framework","slug":"framework","id":2},
#         {"name":"Masaüstü Programlar","slug":"masaustu-programlar","id":3},
#         {"name":"Mobil Programlar","slug":"mobil-programlar","id":4},
#     ]
# }


# Create your views here.


def course_detail(request,deneme):

    
    return render(request,'courses/detail.html',{'course':Course.objects.get(slug=deneme)})


def index(request):

    return render(request,'courses/index.html',{'categories':Category.objects.all(),"courses":Course.objects.all()})

def get_category_by_id(request,category_id):
    
    # return HttpResponse(filtered_data)
    return render(request, 'courses/partials/_courses.html')
    
