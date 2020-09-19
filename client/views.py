from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import posts, feedback
from .models import Comment
from django.http import HttpResponse
from .forms import CommentForm
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credential')
            return redirect('login')
    else:
        return render(request,'login.html')

def reg(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        username= request.POST['username']
        password= request.POST['password']
        password1= request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Address is Taken')
                return redirect('reg')

            else:
                p= User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                p.save();
                print("New User Created")
                return redirect('login')

        else:
            messages.info(request,'Pasword does not match')
            return redirect('reg')
        return redirect('/')
    else:   
        return render(request,'register.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/')

def news(request):
    ac = posts.objects.all()
    return render(request,'news.html',{'pots': ac})

def contract(request):
    if request.method== 'POST':
        if request.POST.get('fed_name') and request.POST.get('email') and request.POST.get('subject') and request.POST.get('note'):
            saverecord=feedback()
            saverecord.fed_name=request.POST.get('fed_name')
            saverecord.email=request.POST.get('email')
            saverecord.subject=request.POST.get('subject')
            saverecord.note=request.POST.get('note')
            saverecord.save()
            messages.info(request,'Form submitted Successfully')
            return render(request,'contact.html')
    else:
            return render(request,'contact.html')


def Post_page(request,id):
    p = posts.objects.get(pk=id)    
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            Parent_obj = None
            try:
                parent_id = int(request.POST.get('comment_id'))
            except:
                parent_id = None
            if parent_id:
                Parent_obj = Comment.objects.get(id = parent_id)
                if Parent_obj:
                    reply_comment = comment_form.save(commit = False)
                    reply_comment.parent = Parent_obj
            new_comment = comment_form.save(commit = False)
            new_comment.post_id_id = id
            new_comment.user_id_id = request.POST['user_id']
            new_comment.save()    
    
    q =Comment.objects.all().filter(post_id = id,parent = None,active = True)
    return render(request,'post_page.html',{'selected_post': p, 'comments': q,})