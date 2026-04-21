from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('category/<int:category_id>/',views.posts_by_category,name='posts_by_category'),
    path('blog/<str:slug>/',views.blog_details,name='blog_details'),    
    path('blog/<int:year>/<int:month>/', views.blogs_list, name='blogs_list'),   
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)