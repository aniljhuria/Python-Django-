from django.shortcuts import render ,redirect,get_object_or_404
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,PostsForm
from django.contrib import messages
from django.template.defaultfilters import slugify

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()

    context={
        'category_count':category_count,
        'blog_count':blog_count
    }
    return render(request,'dashboard/dashboard.html',context)


@login_required(login_url='login')
def categories(request):   
    return render(request,'dashboard/categories.html')



@login_required(login_url='login')
def add_category(request):
    if request.method== 'POST':
        form =CategoryForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('categories')
    
    form=CategoryForm() 
    context={
        'form':form
    }
    return render(request,'dashboard/add_category.html',context)

@login_required(login_url='login')
def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)

    if request.method=="POST":
        form =CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form=CategoryForm(instance=category) 
    context={
        'form':form,
        'category':category
    }
    return render(request,'dashboard/edit_category.html',context)

@login_required(login_url='login')
def delete_category(request ,pk):

    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


# Posts crud 
@login_required(login_url='login')
def posts(request):
    blogs=Blog.objects.all()
    context={
        'blogs':blogs
    }
    return render(request,'dashboard/posts.html',context)


@login_required(login_url='login')
def add_posts(request):
    if request.method== 'POST':
        form =PostsForm(request.POST,request.FILES)
        if form.is_valid():  
            post=form.save(commit=False) # temporaily saving the form
            post.auther=request.user        
            
            post.save()
            return redirect('posts')
        else:
            print(form.errors)
            messages.success(request, form.errors)
            return redirect('posts')
            
    form=PostsForm() 
    context={
        'form':form
    }
    return render(request,'dashboard/add_posts.html',context)


@login_required(login_url='login')
def edit_posts(request,pk):
    blog=get_object_or_404(Blog,pk=pk)

    if request.method=="POST":
        form =PostsForm(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('posts')
    form=PostsForm(instance=blog) 
    context={
        'form':form,
        'blog':blog
    }
    return render(request,'dashboard/edit_posts.html',context)


@login_required(login_url='login')
def delete_posts(request ,pk):

    blog = get_object_or_404(Blog,pk=pk)
    blog.delete()
    return redirect('posts')




