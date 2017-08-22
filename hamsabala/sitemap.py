from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap
from products.models import *
from retail.models import *

class ViewSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)

class SectionMap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5
    
    def items(self):
        return Section.objects.filter(show=True)

    def lastmod(self, obj):
        product = Product.objects.filter(show=True,section=obj.id).order_by("-modified")[0]
        date = product.modified
        if obj.modified > date:
            date = obj.modified
        return date

    def location(self, obj):
        return '/%s/' % obj.slug

class RetailMap(Sitemap):    
    changefreq = 'monthly'
    priority = 0.5
    
    def items(self):
        return City.objects.filter(show=True)

    def lastmod(self, obj):
        product = Partner.objects.filter(show=True,city=obj.id).order_by("-modified")[0]
        date = product.modified
        if obj.modified > date:
            date = obj.modified
        return date

    def location(self, obj):
        return '/retail/%s/' % obj.slug
