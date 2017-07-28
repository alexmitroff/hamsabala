# -*- coding: utf-8 -*-
from django.db import models

class City(models.Model):
    name = models.CharField( "name", max_length = 140,
            blank=True, null=True)
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Partner(models.Model):
    pos = models.IntegerField("position",default=0)
    show = models.BooleanField("show", default = True) 
    name = models.CharField( "name", max_length = 140,
            blank=True, null=True)
    address = model.TextField("address",
            blank=True, null=True)
    city = models.ForeignKey(City, default = 0)
    url = models.CharField( "link", max_length = 250,
            blank=True, null=True)
    
    class Meta:
        verbose_name = u"Partner"
        verbose_name_plural = u"Partners"
        ordering = ["pos"]

    def __str__(self):
        return self.name

