from .models import Category, Blog

def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)



def get_blog_month(request):
    months = Blog.objects.dates('updated_at', 'month', order='DESC')
    return dict(blog_month=months)
