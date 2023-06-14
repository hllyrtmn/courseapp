from datetime import date
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.cache import cache_page


# data={
#     "mobil":"mobil programlama detayları",
#     "masaüstü":"masaüstü programlama detayları",
#     "gömülü-sistemler":"gömülü sistemler detayları",
#     "django":"django detayları",
#     ".net":".net detayları",
# }

db = {
    "courses":[
        {
            "id":1,
            "category_id":1,
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "image_url":"https://images.ctfassets.net/mrop88jh71hl/55rrbZfwMaURHZKAUc5oOW/9e5fe805eb03135b82e962e92169ce6d/python-programming-language.png",
            "slug":"python-kursu",
            "date":date(2023,10,10),
            "is_active":True,
            "is_update":True
        },
        {
            "id":2,
            "category_id":2,
            "title":"angular kursu",
            "description":"angular kurs açıklaması",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Angular_full_color_logo.svg/1200px-Angular_full_color_logo.svg.png",
            "slug":"angular-kursu",
            "date":date(2023,8,10),
            "is_active":True,
            "is_update":False
        },
        {
            "id":3,
            "category_id":1,
            "title":"c# kursu",
            "description":"c# kurs açıklaması",
            "image_url":"https://miro.medium.com/v2/resize:fit:594/1*ymVNbsdd7KxHXHC4-LP7kw.png",
            "slug":"c-sharp-kursu",
            "date":date(2023,3,10),
            "is_active":True,
            "is_update":True
            
        },
        {
            "id":4,
            "category_id":1,
            "title":"java kursu",
            "description":"java kurs açıklaması",
            "image_url":"https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera-course-photos.s3.amazonaws.com/0a/8cd7f1b14344618b75142593bc7af8/JavaCupLogo800x800.png?auto=format%2Ccompress&dpr=1",
            "slug":"java-kursu",
            "date":date(2023,1,10),
            "is_active":True,
            "is_update":True
        },
        {
            "id":5,
            "category_id":3,
            "title":"matlab kursu",
            "description":"matlab kurs açıklaması",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Matlab_Logo.png/800px-Matlab_Logo.png",
            "slug":"matlab-kursu",
            "date":date(2023,12,10),
            "is_active":True,
            "is_update":True
            
        },
        {
            "id":6,
            "category_id":4,
            "title":"mobil excel kursu",
            "description":"mobil excel kurs açıklaması",
            "image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg/1200px-Microsoft_Office_Excel_%282019%E2%80%93present%29.svg.png",
            "slug":"mobil-excel-kursu",
            "date":date(2023,12,5),
            "is_active":True,
            "is_update":False
        },
    ],
    "categories":[
        {"name":"Yazılım Dilleri","slug":"yazilim-dilleri","id":1},
        {"name":"Framework","slug":"framework","id":2},
        {"name":"Masaüstü Programlar","slug":"masaustu-programlar","id":3},
        {"name":"Mobil Programlar","slug":"mobil-programlar","id":4},
    ]
}

# Create your views here.
def index(request):


    return render(request,'courses/index.html',{'categories':db["categories"],"courses":[courses for courses in db["courses"] if courses["is_active"]==True]})

def get_category_by_id(request,category_id):
    data= db["courses"]
    filtered_data = [course for course in data if course.get('category_id')== category_id]
    # return HttpResponse(filtered_data)
    return render(request, 'course/index.html',{'categories':db["categories"],"courses":filtered_data})
    
