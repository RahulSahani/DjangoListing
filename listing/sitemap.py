from django.contrib.sitemaps import Sitemap

from .models import BusinessDetails

class BusinessSitemap(Sitemap):
    changefreq ='weekly'
    priority = 0.9

    def items(self):
        return BusinessDetails.objects.all()
  