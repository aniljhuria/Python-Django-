from django import forms

from blogs.models import Category,Blog
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model =Category
        fields ='__all__'



class PostsForm(forms.ModelForm):
    class Meta:
        model =Blog
        fields =('title','category','feature_image','short_desc','blog_body','status','is_featured')


class UsersForm(UserCreationForm):
    class Meta:
        model =User
        fields =('first_name','last_name','username','email','is_active','is_staff','is_superuser','groups','user_permissions')

   


class EditUserForm(forms.ModelForm):
    class Meta:
        model =User
        fields =('first_name','last_name','username','email','is_active','is_staff','is_superuser','groups','user_permissions')

