
#from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category
from aboutus.models import Aboutus
from django.db.models import Q

def home(request):

    #return HttpResponse('<h2>home page</h2>')
    # categories= Category.objects.all()   
    featured_posts=Blog.objects.filter(is_featured=True,status="Published").order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False,status="Published").order_by('-updated_at')
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