from django.http import HttpResponse

def aboutUs(resuest):
    return HttpResponse("Welcome the page")

def course(request):
    return HttpResponse("<b> Java, Python, SpringBoot, Django <b>")

def course_details(request, course_id):
    return HttpResponse(course_id)