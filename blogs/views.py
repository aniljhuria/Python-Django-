from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from blogs.models import Blog,Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    post=get_object_or_404(Blog,slug=slug,status="Published")
    recent_posts=Blog.objects.filter(status="Published").exclude(slug=slug).order_by('-updated_at')[:3]

    if request.method=="POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please login first for add a  comment")
            return redirect('login')  # login page ka name
        comment=Comment()
        comment.user=request.user
        comment.blog=post
        comment.comment=request.POST['comment']
        comment.save()

        messages.success(request, "Comment Submit Successfully")
        return HttpResponseRedirect(request.path_info)

    #comment
    comments=Comment.objects.filter(blog=post).order_by('-updated_at')
    comments_count=comments.count
   
    context={
        'post':post,
        'recent_posts':recent_posts,
        'comments':comments,
        'comments_count':comments_count
    }    
    return render(request,'blog_details.html',context)


def blogs_list(request,year,month):

    posts = Blog.objects.filter(
        status="Published",
        created_at__year=year,
        created_at__month=month
    )
    recent_posts=Blog.objects.filter(status="Published").order_by('-updated_at')[:3]
    
    context={
        'posts':posts,
        'recent_posts':recent_posts,
    }    
    return render(request,'blogs_list.html',context)










