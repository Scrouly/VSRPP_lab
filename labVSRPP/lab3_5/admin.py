from django.contrib import admin

from .models import Students, Groups, Faculty

admin.site.register(Students)

admin.site.register(Groups)
admin.site.register(Faculty)
# Register your models here.
