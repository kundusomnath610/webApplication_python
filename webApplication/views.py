from django.http import HttpResponse
from django.shortcuts import render

"""
    render needs two parameter resuest and what page we want to render
"""
def home(resuest):
    return render(resuest, "index.html") 

def aboutUs(resuest):
    return HttpResponse("Welcome the page")

def course(request):
    return HttpResponse("<b> Java, Python, SpringBoot, Django <b>")

def course_details(request, course_id):
    return HttpResponse(course_id)