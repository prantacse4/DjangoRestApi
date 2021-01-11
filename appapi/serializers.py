from rest_framework import  serializers
from .models import MyApi

class MyApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyApi
        fields = "__all__"