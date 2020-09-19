from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vlog(request):
    return HttpResponse("Hello World")