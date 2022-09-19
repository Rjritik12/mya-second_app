from rest_framework import serializers
from .models import *

class StudenSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True, max_length=100)
    salary =  serializers.CharField(required=False, allow_blank=True, max_length=100)
    post =  serializers.CharField(required=False, allow_blank=True, max_length=100)
    class Meta:
        model = Emp
        fields = ['name','salary','post']