from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from bakery.models import BuildableModel

# Create your models here.

def collection_path(instance, filename):
	filename = filename.replace(" ", "")
	if len(filename) > 100:
		filename = filename[:99]
	return 'collectons/{0}/{1}'.format(instance.url, filename)

class Collection(BuildableModel):
    detail_views = ('landing.build.CollectionView')
    pos = models.IntegerField(u'позиция', default=0, help_text=u"От меньшего к большему")
    show = models.BooleanField(u"показывать", default=True)
    title = models.CharField(u'название', max_length=140)
    url = models.CharField('url', max_length=20, default="ivanov")
    created = models.DateField(u'дата создания',auto_now=False, auto_now_add=True)
    modefied = models.DateField(u'дата изменения',auto_now=True, auto_now_add=False)
    img = models.ImageField(u'обложка', upload_to=collection_path)

    class Meta:
        verbose_name=u"коллекция"
        verbose_name_plural=u"коллекции"
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
