from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('',views.testimonial,name='testimonial'),
    path('news_blog',views.news_blog,name='news_blog')
]