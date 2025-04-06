
from django.urls import path
from recipes.views import home,contato,my_view


urlpatterns = [
    path('', my_view),
    path('home/',home),
    path('contato/',contato),
]
