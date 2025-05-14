from django.shortcuts import render
from django.http import HttpResponse,Http404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe

# Create your views here.
 

def home(request):
    recipes = Recipe.objects.filter(is_publish = True).order_by('-id')
    return render(request,'pages/home.html', context={
        
        'recipes':recipes,
        
    })




def category(request,category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_publish = True
        ).order_by('-id')
    ''' 
    category_name = getattr(getattr(recipes.first(), 'category', None),
                    'name','Not found')
    '''
    if not recipes:
        raise Http404('Not Found 😘')
    return render(request,'pages/category.html', context={
        'recipes':recipes,
        'title':  f'{recipes.first().category.name} - Category | ' ,
    })


def recipes(request,id):
    return render(request,'pages/recipe-view.html', context={
        'recipe':make_recipe(),
        'is_detail_page': True,
        })