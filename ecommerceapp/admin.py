from django.contrib import admin
from .models import Category,Doctor


# Register your models here
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'img','charge','category']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Doctor,DoctorAdmin)

