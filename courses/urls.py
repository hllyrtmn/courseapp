from django.urls import path

from courses import views


urlpatterns = [
    path('',views.home),
    path('anasayfa',views.home),
    path('kurslar',views.courses)
    
    
]
