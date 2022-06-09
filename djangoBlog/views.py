from django.shortcuts import render
from django.shortcuts import HttpResponse

def about (request):
    return render(request,'About.html')
def home(request):
    return HttpResponse('Home.html')
