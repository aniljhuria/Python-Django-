from django import forms

from blogs.models import Category,Blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model =Category
        fields ='__all__'



class PostsForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields =('title','category','feature_image','short_desc','blog_body','status','is_featured')