from bakery.views import BuildableTemplateView 
from bakery.views import BuildableDetailView 
import os
from landing.models import *
from django.conf import settings

class IndexView(BuildableTemplateView):
    build_path = 'index.html'
    template_name = 'pages/indexs.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['collections'] = Collection.objects.filter(show = True)
	return context

class CollectionView(BuildableDetailView):
    queryset = Collection.objects.filter(show = True)
    template_name = 'pages/collection.html'
    
    def get_build_path(self, obj):
        path = os.path.join(settings.BUILD_DIR, self.get_url(obj)[1:])
        os.path.exists(path) or os.makedirs(path)
        return os.path.join(path, obj.url+".html")
