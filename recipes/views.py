from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def home(request):
    return HttpResponse('home do views ')

def contato(request):
    return HttpResponse('contato')
    
def my_view(request):
    return render(request,'recipes/home.html')
