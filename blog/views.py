from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . models import MyBlog
from .  import forms
from django.contrib.auth import login, logout


# Create your views here.
#@login_required(login_url="signup:home")
def bloglist(request):
    blogs = MyBlog.objects.all().order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})

#@login_required(login_url="signup:home")
def blogpost(request, slug): 
    blog=MyBlog.objects.filter(slug=slug).first()
    return render(request, "blogpost.html", {'blog':blog})

#@login_required(login_url="signup:home")
def politics(request):
    blogs = MyBlog.objects.all().filter(category='politics').order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})
#@login_required(login_url="signup:home")
def sports(request):
    blogs = MyBlog.objects.all().filter(category='Sports').order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})
#@login_required(login_url="signup:home")
def business(request):
    blogs = MyBlog.objects.all().filter(category='Business').order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})
#@login_required(login_url="signup:home")
def education(request):
    blogs = MyBlog.objects.all().filter(category='Education').order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})
#@login_required(login_url="signup:home")
def other(request):
    blogs = MyBlog.objects.all().filter(category='Other').order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})
#@login_required(login_url="signup:home")
def entertainment(request):
    blogs = MyBlog.objects.all().filter(category='Entertainment').order_by('-datetime')
    return render(request,'blog.html',{'blogs':blogs})

#@login_required(login_url="signup:home")
def create(request):
    form = forms.OwnBlog()
    if request.method == 'POST':
        form = forms.OwnBlog(request.POST, request.FILES)
        if form.is_valid():
            context = form.save(commit = False)
            context.author = request.user
            context.save()
            return redirect('blog:bloglist')
    return render(request,'your_blog.html',{'form':form}) 
#@login_required(login_url="signup:home")    
def profile(request):
    blogs = MyBlog.objects.all().filter(author = request.user).order_by('-datetime')
    total = MyBlog.objects.all().filter(author = request.user).count()
    if(total == 0):
        numberofblogs = True
    else:
        numberofblogs = False


    # if request.method=='POST':
    return render(request, 'myblog.html',{'blogs':blogs,'total':numberofblogs})
#@login_required(login_url="signup:home")
def logout_view(request):
    logout(request)
    return redirect('signup:home')



 

