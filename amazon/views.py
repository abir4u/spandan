from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination,Testimonial,News
from .forms import News_Post
# Create your views here.
def home(request):
    
    dests = Destination.objects.all()
    tests = Testimonial.objects.all()
    news = News.objects.all()
    return render(request, 'index.html',{'dests': dests,'tests': tests, 'news': news,})
    

def about(request):
    return render(request,'about.html')

def testimonial(request):
    
    return render(request, 'index.html',)

def news_blog(request):
    form = News_Post(request.POST or None,request.FILES)
    
    return render(request,'blog.html')