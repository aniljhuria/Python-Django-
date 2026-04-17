from django.db import models

# Create your models here.

class Aboutus(models.Model):
    about_heading =models.CharField(max_length=30)
    about_desc=models.TextField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='About Us'

    def __str__(self):
        return self.about_heading
