from django.shortcuts import render
from landing.models import *

# Create your views here.

def index(request):
    template = 'pages/index.html'
    collections = Collection.objects.filter(show=True)
    var = {"collections":collections}
    return render(request, template, var)
