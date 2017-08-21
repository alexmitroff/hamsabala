from django.shortcuts import render
from django.shortcuts import get_object_or_404

from products.models import *
from retail.models import *

import urllib.request
import json
# Create your views here.

class Instaphoto:
    img = ''
    url = ''
    caption = ''

    def set_img(self, picture):
        self.img = picture
    
    def set_url(self, link):
        self.url = link
    
    def set_caption(self, text):
        self.caption = text
    
    def __init__(self, name):
        self.code = name


def str2obj():
    url = 'https://www.instagram.com/hamsabala.pro/media/'
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req).read()
    insta_raw = json.loads(r.decode('utf-8'))
    objs = []
    i = 0
    for item in insta_raw['items']:
        o = Instaphoto(item['code'])
        o.set_img(item['images']['standard_resolution']['url'])
        o.set_url(item['link'])
        o.set_caption(item['caption']['text'])

        if i > 3:
            break
        else:
            objs.append(o)
        
        i += 1
    
    return objs

def index(request):
    template = 'pages/index.html'
    sections = Section.objects.filter(show=True)
    cities = City.objects.filter(show=True)
    retail = []
    for c in cities:
        item = {}
        item["shops"] = Partner.objects.filter(show=True, frontpage=True, city=c.pk)[:3]
        item["city"] = c
        item["more"] = False
        if Partner.objects.filter(show=True, city=c.pk).count() > 3:
            item["more"] = True
        retail.append(item)

    var = {
            "sections":sections,
            "retail":retail,
            }
    return render(request, template, var)

def section(request, section):
    template = 'pages/section.html'
    section = get_object_or_404(Section, slug=section)
    collections = Collection.objects.filter(show=True)
    products = []
    for c in collections:
        p = Product.objects.filter(show=True, section=section, collection=c)
        products.append({"collection":c, "products":p})
    var = {
            "section":section,
            "collections":products,
            }
    return render(request, template, var)

def constraction(request):
    template = 'pages/constraction.html'
    var = {}
    return render(request, template, var)

def retail(request, city):
    template = 'pages/retail.html'
    city = City.objects.filter(slug=city).first()
    cities = City.objects.filter(show=True)
    shops = Partner.objects.filter(show=True, city=city.pk).order_by('name')
    var = {
            "city":city,
            "cities":cities,
            "shops":shops,
            }
    return render(request, template, var)

def feedback(request):
    return False 
