from django.shortcuts import render
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
    template = 'pages/constraction.html'
    sections = Section.objects.filter(show=True)
    var = {
            "sections":sections,
            }
    return render(request, template, var)

def constraction(request):
    template = 'pages/constraction.html'
    var = {}
    return render(request, template, var)
