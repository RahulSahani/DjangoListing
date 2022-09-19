from rest_framework import serializers
from .models import *

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDetails

        fields = '__all__'
        