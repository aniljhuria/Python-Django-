from django.contrib import admin
from .models import Aboutus


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self,request):
        count=Aboutus.objects.all().count()
        if count == 0:
            return True
        return False

# Register your models here.

admin.site.register(Aboutus,AboutAdmin)