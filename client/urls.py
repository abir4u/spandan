from django.urls import path
from . import views

urlpatterns = [
    path('reg',views.reg,name='reg'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('news',views.news,name='news'),
    path('contract',views.contract,name='contract'),
    path('news/Post_page/<int:id>/',views.Post_page,name='Post_page'),
]