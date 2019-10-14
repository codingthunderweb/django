from django.http import HttpResponse
from django.shortcuts import *

def about(request):
    #return HttpResponse("this is my site")
    return render(request,'about.html')
def home(request):
    #return HttpResponse("Homepage")
    return render(request,'homepage.html')