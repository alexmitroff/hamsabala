# -*- coding: utf-8 -*-
from django.db import models

class City(models.Model):
    pos = models.IntegerField("position",default=0)
    show = models.BooleanField("show", default = True) 
    name = models.CharField( "name", max_length = 140,
            blank=True, null=True)
    slug = models.SlugField('slug', max_length=50,
            help_text="http://hamsabala.ru/slug/slug")
    created = models.DateField(u'created',auto_now=False, 
            auto_now_add=True)
    modified = models.DateField(u'modified',auto_now=True, 
            auto_now_add=False)
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["pos"]

    def __str__(self):
        return self.name

class Partner(models.Model):
    pos = models.IntegerField("position",default=0)
    show = models.BooleanField("show", default = True) 
    frontpage = models.BooleanField("frontpage", default = False, help_text="Show on front page") 
    name = models.CharField( "name", max_length = 140,
            blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,
            default = 0)
    address = models.TextField("address",
            blank=True, null=True)
    url = models.CharField( "link", max_length = 250,
            blank=True, null=True)
    created = models.DateField(u'created',auto_now=False, 
            auto_now_add=True)
    modified = models.DateField(u'modified',auto_now=True, 
            auto_now_add=False)
    
    class Meta:
        verbose_name = u"Partner"
        verbose_name_plural = u"Partners"
        ordering = ["pos"]

    def __str__(self):
        return self.name

