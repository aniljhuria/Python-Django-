from .models import Category, Blog
from django.db.models import Count

def get_categories(request):
    #categories=Category.objects.all().order_by('-id')[:8]
    categories = Category.objects.annotate(
            post_count=Count('blog')   # related_name ya default blog_set
        ).order_by('-post_count')[:8]
    return dict(categories=categories)



def get_blog_month(request):
    months = Blog.objects.dates('created_at', 'month', order='DESC')
    return dict(blog_month=months)
