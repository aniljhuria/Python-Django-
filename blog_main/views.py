
#from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blogs.models import Blog, Category
from aboutus.models import Aboutus
from django.db.models import Q
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.core.paginator import Paginator

def home(request):

    #return HttpResponse('<h2>home page</h2>')
    # categories= Category.objects.all()   
    featured_posts=Blog.objects.filter(is_featured=True,status="Published").order_by('updated_at')   
    posts=Blog.objects.filter(is_featured=False,status="Published").order_by('-updated_at')  

    paginator = Paginator(posts, 4)  # 6 per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    try:
        about_us=Aboutus.objects.get()
    except:
        about_us=None

    context={
        # 'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
        'about_us':about_us
    }
    return render(request,'home.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    blog=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword) | Q(blog_body__icontains=keyword),status="Published")
    recent_posts=Blog.objects.filter(status="Published").exclude(Q(title__icontains=keyword) | Q(short_desc__icontains=keyword) | Q(blog_body__icontains=keyword)).order_by('-updated_at')[:3]
    
    context={        
        'blog':blog,
        'recent_posts':recent_posts,
        'keyword':keyword
    }
    return render(request ,'search.html',context)


def register(request):
    if request.method== 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Registered")
            return redirect('register')        
    else:
        form=RegistrationForm()

    context={
            'form':form
    }
    return render(request,'register.html', context)


def login(request):
    if request.method== 'POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)            
            messages.success(request, "Successfully login")
            return redirect('dashboard')        
    else:
        form=AuthenticationForm()

    context={
            'form':form
    }
    return render(request,'login.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('home')


def custom_403(request, exception):
    return render(request, '403.html', status=403)

    