from django.urls import path

from courses import views


urlpatterns = [
    path('',views.index),
    path('kategoriler/<int:category_id>',views.category_by_id),
    path('kategoriler/<str:category>',views.get_courses_by_cname,name='category_by_id'),
]
