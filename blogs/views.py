from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blogs.models import Blog

# Create your views here.


def posts_by_category(request,category_id):
   
    posts=Blog.objects.filter(category=category_id,status="Published")
    recent_posts=Blog.objects.filter(status="Published").exclude(category=category_id).order_by('-updated_at')[:3]

    # try:
    #      categories_data= Category.objects.get(pk=category_id)
    # except:
    #      return redirect('home')
    
    # category_data=get_object_or_404(Category,pk=category_id)

    context={
        'posts':posts,
        # 'categories':categories,
        'recent_posts':recent_posts,
    }    
    return render(request,'post_by_category.html',context)



def blog_details(request,slug):    
     
    # post=Blog.objects.get(slug=slug,status="Published")
    post=get_object_or_404(Blog,slug=slug,status="Published")
    recent_posts=Blog.objects.filter(status="Published").exclude(slug=slug).order_by('-updated_at')[:3]
    
    context={
        'post':post,
        'recent_posts':recent_posts,
    }    
    return render(request,'blog_details.html',context)


def blogs_list(request,year,month):

    posts = Blog.objects.filter(
        status="Published",
        updated_at__year=year,
        updated_at__month=month
    )
    recent_posts=Blog.objects.filter(status="Published").order_by('-updated_at')[:3]
    
    context={
        'posts':posts,
        'recent_posts':recent_posts,
    }    
    return render(request,'blogs_list.html',context)


