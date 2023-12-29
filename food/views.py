from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader


# Create your views here.
def index(request):
    
    context = {
        'item_list': Item.objects.all()}
    
    return render(request, 'food/index.html' , context)

def item(request):
    return HttpResponse('<h1> teg h1 </h1>')

# path('<int:item_id>/'
def detail(request, item_id):
   
    context = {
        "item": Item.objects.get(id = item_id)
       
    }

    return render(request, 'food/detail.html' , context)

