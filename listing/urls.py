from django.urls import path , include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView



from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('api', views.Businessviewset , basename="snippets")



urlpatterns = [

        path('', views.home_view , name='home'),
        path('add-listing' , views.Add_listing , name='add-listing' ),
        # path('about' ,views.About_us , name='about'),
        path('contact' , views.Contact_us , name='contact-us'),
        path("blog/<slug:slug>", views.single_view , name='single_view'),
        # path('list/<slug:slug>/' , views.Listing_Details , name='listing-details'),
        path('blog' ,views.Blog , name='blog'),
        path('listing-list' ,views.listing , name='listing'),
        path('animal-clinic/<slug:slug>/' , views.Listing_Details.as_view() , name='listing-details'),
        path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),
        path('data/', include(router.urls)),
        path('state/<slug:slug>' , views.State , name='state'),
         path('city/<slug:slug>' , views.city , name='city'),

] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
