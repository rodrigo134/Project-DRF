
from django.urls import path
from recipes.views import home
from . import views


#recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('', views.home,name="home"),
    path('recipes/<int:id>',views.recipes,name="recipe")
]
