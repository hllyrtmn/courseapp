from django.urls import path

from courses import views


urlpatterns = [
    path('',views.index),
    path('kategoriler/<int:category_id>',views.get_category_by_id,name="category_id"),
    path('<str:deneme>',views.course_detail,name="detail_page"),
    path('kurslar/',views.index),
]
