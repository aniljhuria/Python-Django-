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

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.helper = FormHelper()        
    #     self.helper.form_method = 'post'      

    #     self.helper.layout = Layout(
    #         Row(
    #             Column('first_name', css_class='form-group col-md-6'),
    #             Column('last_name', css_class='form-group col-md-6'),
    #         ),
    #         Row(
    #             Column('username', css_class='form-group col-md-6'),
    #             Column('email', css_class='form-group col-md-6'),
    #         ),            
    #         Row(
    #             Column('is_active'),
    #             Column('is_staff'),
    #             Column('is_superuser'),
    #         ),
             #Row(
    #             Column('groups', css_class='form-group col-md-6'),
    #             Column('user_permissions', css_class='form-group col-md-6'),
    #         ),
            # Row(
    #             Column('password1', css_class='form-group col-md-6'),
    #             Column('password2', css_class='form-group col-md-6'),
    #         ),    
    #         Submit('submit', 'Save User', css_class='btn btn-warning')
    #     )


class EditUserForm(forms.ModelForm):
    class Meta:
        model =User
        fields =('first_name','last_name','username','email','is_active','is_staff','is_superuser','groups','user_permissions')

