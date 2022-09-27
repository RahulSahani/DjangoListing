from rest_framework import serializers
from .models import *

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetails

        fields = '__all__'
        

# # I will show you a pseudo code then you can search the sentaxt ok ? its easy  i took ideas from blgs and articles to develop this i don't have prior experience
# #https://django.fun/en/qa/428148/ check here , I wish i can help but my time in short , i understand Thank you for your time , i am sorry but couldn't getting this
# #please help i know you have limited time ?? Im checking 
# class checkmySlug(serializers.slug):
#     slug = BusinessDetails.objects.all()
#     #this will check the slug 
#     if slug == slug:
#         return slug 
#     else:
#         pass
    

# class SnippetSerializer(serializers.ModelSerializer):
#     new_slug = checkmySlug()   # write a method that checks if slug exist and return
#     # I really can't remmebr the exact code right now 
# # you can't do this , you need to get serializer.data['slug' comthing like this,]
#     BusinessDetails.objects.get()
#     class Meta:
#         model = BusinessDetails

#         fields = ['title', 'new_slug', '', '', '' ......etc]

#         # good news .. Note that there exists an AutoSlugField in the django-extensions package [PyPi], that automates this slug procedure. For example: 
#         # read here , you can solve this from your model :) wait let me get you the link 
#         #https://stackoverflow.com/questions/57147034/how-to-change-slug-if-same-string-is-stored-in-it

