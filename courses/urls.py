from django.urls import path

from courses import views


urlpatterns = [
    path('',views.courses),
    path('liste',views.courses),
    path('detaylar',views.details),
    # path('programlama',views.programming), dinamik hale getirerek metod tanımlamasından kurtulduk
    # path('mobil-uygulamalar',views.mobile_app), bir alt satırdaki yaptığımız gibi
    path('<category>',views.get_courses_by_cname)
]
