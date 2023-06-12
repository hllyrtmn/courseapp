from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def courses(request):
    return HttpResponse("kurslar sayfası")
def details(request):
    return HttpResponse("detaylar sayfası")
def programming(request):
    return HttpResponse("programlama sayfası")
def mobile_app(request):
    return HttpResponse("mobil uygulama sayfası")