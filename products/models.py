from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

def section_path(instance, filename):
	filename = filename.replace(" ", "")
	if len(filename) > 100:
		filename = filename[:99]
	return 'sections/{0}/{1}'.format(instance.url, filename)

class Section(models.Model):
    pos = models.IntegerField(u'position', default=0)
    show = models.BooleanField(u"show", default=True)
    title = models.CharField(u'name', max_length=140)
    slug = models.SlugField('slug', max_length=50,
            help_text="http://hamsabala.ru/slug/slug")
    created = models.DateField(u'created',auto_now=False, 
            auto_now_add=True)
    modified = models.DateField(u'modified',auto_now=True, 
            auto_now_add=False)
    img = models.ImageField(u'cover', upload_to=section_path,
            blank=True, null=True)

    class Meta:
        verbose_name=u"section"
        verbose_name_plural=u"sections"
        ordering = ['pos']
    
    def save(self, *args, **kwargs):
        try:
            this = Section.objects.get(id=self.id)
            if this.img != self.img:
                this.img.delete(save=False)
        except:
            pass
        super(Section, self).save(*args, **kwargs)
    def  __str__(self):
        return self.title

@receiver(pre_delete, sender=Section)
def section_delete(sender, instance, **kwargs):
	instance.img.delete(False)

def collection_path(instance, filename):
	filename = filename.replace(" ", "")
	if len(filename) > 100:
		filename = filename[:99]
	return 'collectons/{0}/{1}'.format(instance.url, filename)

class Collection(models.Model):
    pos = models.IntegerField(u'position', default=0)
    show = models.BooleanField(u"show", default=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=0)
    title = models.CharField(u'name', max_length=140)
    slug = models.SlugField('slug', max_length=50,
            help_text="http://hamsabala.ru/slug/slug")
    created = models.DateField(u'created',auto_now=False,
            auto_now_add=True)
    modified = models.DateField(u'modified',auto_now=True,
            auto_now_add=False)
    img = models.ImageField(u'cover',
            upload_to=collection_path,
            blank=True, null=True)
    color = models.CharField(u'color', max_length=6, 
            help_text="HEX number. 23dvr1 for example.")

    class Meta:
        verbose_name=u"collection"
        verbose_name_plural=u"collections"
        ordering = ['pos']
    
    def save(self, *args, **kwargs):
        try:
            this = Collection.objects.get(id=self.id)
            if this.img != self.img:
                this.img.delete(save=False)
        except:
            pass
        super(Collection, self).save(*args, **kwargs)
    def  __str__(self):
        return self.title

@receiver(pre_delete, sender=Collection)
def collection_delete(sender, instance, **kwargs):
	instance.img.delete(False)

def product_path(instance, filename):
	filename = filename.replace(" ", "")
	if len(filename) > 100:
		filename = filename[:99]
	return 'products/{0}/{1}'.format(instance.url, filename)

class Product(models.Model):
    pos = models.IntegerField(u'position', default=0)
    show = models.BooleanField(u"show", default=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, 
            default=0)
    name = models.CharField( "name", max_length = 140,
            blank=True, null=True)
    description = models.TextField("description",
            blank=True, null=True)
    price = models.DecimalField(u'price', max_digits=6, decimal_places=2)
    img = models.ImageField(u'cover',
            upload_to=collection_path,
            blank=True, null=True)
    created = models.DateField(u'created',auto_now=False, 
            auto_now_add=True)
    modified = models.DateField(u'modified',auto_now=True, 
            auto_now_add=False)

    class Meta:
        verbose_name=u"product"
        verbose_name_plural=u"products"
        ordering = ['collection','pos']
    
    def save(self, *args, **kwargs):
        try:
            this = Product.objects.get(id=self.id)
            if this.img != self.img:
                this.img.delete(save=False)
        except:
            pass
        super(Product, self).save(*args, **kwargs)
    def  __str__(self):
        return "%s %s" % (self.collection.title, self.name)
