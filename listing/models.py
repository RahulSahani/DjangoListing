from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
# Create your models here.

class CountryPage(models.Model):
    country_Name = models.CharField(max_length=255)
    slug =  models.SlugField(unique=True , max_length=255 , null=True , blank=True)
    description = models.TextField()

    def __str__(self):
        return self.country_Name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.country_Name)
        super().save(*args, **kwargs)

class StatePage(models.Model):
    stateName = models.CharField(max_length=255 , unique=True)
    slug =  models.SlugField(unique=True , max_length=255 , null=True , blank=True)
    stateImage = models.ImageField(upload_to='state' , blank=True ,null=True)
    country = models.ForeignKey(CountryPage , on_delete=models.SET_NULL , blank=True, null=True)
    def __str__(self):
        return self.stateName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.stateName)
        super().save(*args, **kwargs)

class City(models.Model):
    cityName = models.CharField(max_length=255 , blank=True, null=True)
    slug =  models.SlugField(unique=True , max_length=255 , null=True , blank=True)
    state = models.ForeignKey(StatePage , on_delete=models.SET_NULL , blank=True , null=True)

    def __str__(self):
        return self.cityName

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cityName)
        super().save(*args, **kwargs)


class BlogCategory(models.Model):
    title = models.CharField(max_length=255)
    slug =  models.SlugField(unique=True , max_length=255 , null=True , blank=True)
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
class Post(models.Model):

    status = [
        (0,'Draft'),
        (1 , 'Published')
    ]
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True , max_length=255 , null=True , blank=True)
    content = RichTextField(null=True , blank=True)
    postStatus = models.IntegerField(choices=status , default=0)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(BlogCategory , on_delete=models.SET_NULL , blank=True, null=True)
    featured_image = models.ImageField(upload_to='blog' , blank=True , null=True)
    def __str__(self):
       return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class BusinessDetails(models.Model):
    title = models.CharField(max_length=500 , blank=True , null=True)
    slug =  AutoSlugField(populate_from='title')
    # slug = models.CharField(unique=True , max_length=255 , null=True , blank=True)
    description = RichTextField(null=True , blank=True)
    address = RichTextField(null=True , blank=True)
    website = models.CharField(max_length=255 , null=True , blank=True)
    phone = models.CharField(max_length=255 , null=True , blank=True)
    rating = models.FloatField(null=True , blank=True)
    reviews = models.CharField(max_length=255 , null=True , blank=True)
    profile_image = models.ImageField(upload_to='uploads' , blank=True , null=True)
    state = models.ForeignKey(StatePage, related_name = 'state' ,on_delete=models.SET_NULL , blank=True, null=True , )
    country = models.ForeignKey(CountryPage ,on_delete=models.SET_NULL , blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET , blank=True, null=True)
    time = models.CharField(max_length=2000 , blank=True , null=True)
   
    def __str__(self):
       return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("listing-details", kwargs={"slug": self.slug})
    

class AddListingRequest(models.Model):
    clinicName = models.CharField(max_length=500)
    description =  models.TextField(blank=True , null=True)
    clinicTiming = models.TextField(blank=True , null=True)
    address = models.TextField(blank=True , null=True)
    ownerName = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    phone = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    image = models.ImageField(upload_to='addListing')
    city = models.CharField(max_length=255 , blank=True , null=True)
    state = models.CharField(max_length=255 , blank=True , null=True)

    def __str__(self):
        return self.clinicName
    
class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1200)
    monday = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name
     

class LeadsForClinic(models.Model):
    clinicName = models.CharField(max_length=255 , blank=True , null=True)
    clientName = models.CharField(max_length=255 , blank=True , null=True)
    clientPhone = models.CharField(max_length=255 , blank=True , null=True)
    AppointmentDate = models.DateField(null=True , blank=True)

    def __str__(self):
       return self.clinicName