from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blogs.models import Blog, Category
# Create your views here.


def posts_by_category(request,category_id):

    # categories= Category.objects.all()   
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
    
    # categories= Category.objects.all()   
    post=Blog.objects.get(slug=slug,status="Published")
    recent_posts=Blog.objects.filter(status="Published").exclude(slug=slug).order_by('-updated_at')[:3]
    
    context={
        'post':post,
        # 'categories':categories,
        'recent_posts':recent_posts,
    }    
    return render(request,'blog_details.html',context)
