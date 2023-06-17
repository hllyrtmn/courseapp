from django.urls import path

from courses import views


urlpatterns = [
    path('',views.index),
    path('search',views.search,name="search"),
    path('create',views.create,name="create"),
    path('<slug:slug>',views.course_detail,name="detail"),
    path('category/<slug:slug>',views.get_course_by_category,name="course_by_category"),
]
