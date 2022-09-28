from django.contrib.sitemaps import Sitemap

from .models import *

class BusinessSitemap(Sitemap):
    changefreq ='weekly'
    priority = 0.9

    def items(self):
        return BusinessDetails.objects.all()[0:4]

    def lastmod(self, obj):
        return obj.modified

class PostSitemap(Sitemap):
    changefreq ='weekly'
    priority = 0.9
    
    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.modified

class StateSitemap(Sitemap):
    changefreq ='weekly'
    priority = 0.9
    
    def items(self):
        return StatePage.objects.all()

class CitySitemap(Sitemap):
    changefreq ='weekly'
    priority = 0.9
    
    def items(self):
        return City.objects.all()