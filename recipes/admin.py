from django.contrib import admin
from .models import Category, Recipe
# Register your models here.


#a way of doing    
@admin.register(Recipe)    
class RecipeAdmin(admin.ModelAdmin):
    ...
    
    

#a way of doing
class CategoryAdmin(admin.ModelAdmin):
    ...
admin.site.register(Category, CategoryAdmin)