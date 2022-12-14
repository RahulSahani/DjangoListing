from calendar import MONDAY
from django.shortcuts import render ,get_object_or_404
from .models import *
from django.db.models import Count
from django.views.generic.detail import DetailView
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication 

from django.contrib.auth.models import User

def home_view(request):
    city_count = StatePage.objects.annotate(num_of_city=Count('city'))
    # states = StatePage.objects.all()
    blogPosts = Post.objects.filter(postStatus = 1)
    business = BusinessDetails.objects.all()[0:6]
    context = {'blogPosts':blogPosts , 'business':business , 'cities':city_count}
    return render( request, 'blog/index.html', context)

def single_view(request , slug):
    blogPost = Post.objects.get(slug=slug)
    context ={'blogPost':blogPost}
    return render( request, 'blog/post.html', context)

def Contact_us( request):
    if request.method == 'POST':
        name = request.POST['fname'] + ' ' + request.POST['lname']
        phone = request.POST['phone'] 
        email = request.POST['email'] 
        subject = request.POST['subject'] 
        message = request.POST['message'] 
        print(name, phone, email, subject, message )
        contact = ContactUs(name=name, phone=phone, email=email, subject=subject , message=message)
        contact.save()

    context = {}
    return render( request, 'blog/contact.html', context)

# def Listing_Details(request , slug):
#     business = BusinessDetails.objects.get(slug=slug)
#     context = {'business':business}
#     return render( request, 'blog/listing-details-1.html', context)

class Listing_Details(DetailView):
    model = BusinessDetails
    template_name = 'blog/listing-details-1.html'



def listing(request):
    businessList = BusinessDetails.objects.all()
    context = {'businessLists':businessList}
    return render( request, 'blog/listing-list.html', context)

def Add_listing(request):

    if request.method == 'POST':
        clinic = request.POST['Clinicname']
        description = request.POST['discription']
        clinicTiming = request.POST['ClinicTiming']
        address = request.POST['ClinicAddress']
        ownerName = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        website = request.POST['website']
        image = request.POST['Image']
        city = request.POST['city']
        state = request.POST['state']
        addListDetails = AddListingRequest(clinicName = clinic , description = description,clinicTiming = clinicTiming ,address = address, ownerName = ownerName, email =email,phone = phone, website = website, image =image , city = city, state= state)
        addListDetails.save()

    context = {}
    return render( request, 'blog/add-listing.html', context)

# def About_us( request):
#     context = {}
#     return render( request, 'blog/about.html', context)


def Blog(request):
    blogPost = Post.objects.all()
    context = {'blogPost':blogPost}
    return render( request, 'blog/blog.html', context)


def State(request ,slug):
    # state = StatePage.objects.filter(slug=slug)
    state = get_object_or_404(StatePage, slug=slug)
    cities = City.objects.filter(state=state.pk)
    business = BusinessDetails.objects.filter(state=state.pk)
    context = {'state':state , 'cities':cities , 'business':business}
    return render( request, 'blog/state.html', context)



def city(request , slug):
    city = get_object_or_404(City, slug=slug)
    business = BusinessDetails.objects.filter(city=city.pk)
    context = {'city':city , 'business':business,}
    return render(request, 'blog/city.html', context)
 


def Leads( request):
    if request.method == 'POST':
        clinicName = request.POST['clinicName'] 
        clientName = request.POST['clientName'] 
        clientPhone = request.POST['clientPhone'] 
        AppointmentDate = request.POST['AppointmentDate'] 
        leads = LeadsForClinic(clinicName=clinicName, clientName=clientName, clientPhone=clientPhone, AppointmentDate=AppointmentDate)
        print(clinicName, clientName, clientPhone)
        leads.save()

    context = {}
    return render( request, 'blog/index.html', context)



from rest_framework import viewsets

from .serializers import *

class Businessviewset(viewsets.ModelViewSet):

     serializer_class = SnippetSerializer
     queryset = BusinessDetails.objects.all()
     authentication_classes = [TokenAuthentication]
     permission_classes = [IsAuthenticated]


