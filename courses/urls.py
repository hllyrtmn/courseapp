from django.urls import path

from courses import views


urlpatterns = [
    path('',views.index),
    path('kategoriler/<int:category_id>',views.get_category_by_id,name="category_id"),
    path('<slug:slug>',views.course_detail,name="detail"),
    path('kurslar/',views.index),
]
