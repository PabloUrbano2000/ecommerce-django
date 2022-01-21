from django.contrib import admin

from category.models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # con esto autorrellenamos campos
    prepopulated_fields= {'slug': ('category_name',)}
    list_display=('category_name', 'slug')

admin.site.register(Category, CategoryAdmin)
