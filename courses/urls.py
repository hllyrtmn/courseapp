from django.urls import path

from courses import views


urlpatterns = [
    path('',views.courses),
    path('liste',views.courses),
    path('detaylar',views.details),
    path('programlama',views.programming),
    path('mobil-uygulamalar',views.mobile_app),
]
