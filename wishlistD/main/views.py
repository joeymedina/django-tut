from django.shortcuts import render
from django.http import HttpResponse
from .models import WishList,Item

# Create your views here.

def index(response, id):
    ls= WishList.objects.get(id=id)
    items = ls.item_set.get(id=1)
    return HttpResponse("<h1>Welcome to %s</a><br><p>%s - $%d</p>" % (ls.name, items.item_name, items.price))


