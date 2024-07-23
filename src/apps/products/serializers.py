from rest_framework import serializers
from .models import *

class UploadImagePhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model=UploadImagePhone
        fields=['pk' , 'file']
    
    def to_representation(self, instance):
        return instance.file.url

class PhoneSerializer(serializers.ModelSerializer):
    images=serializers.SerializerMethodField()

    class Meta:
        model=Phone
        fields="__all__"

    def get_images(self,obj):
        images=obj.image.all()
        return UploadImagePhoneSerializer(instance=images , many=True ).data
    

class UploadImageLaptopSerializer(serializers.ModelSerializer):

    class Meta:
        model=UploadImageLaptop
        fields=['pk' , 'file']
    
    def to_representation(self, instance):
        return instance.file.url

class LaptopSerializer(serializers.ModelSerializer):

    images=serializers.SerializerMethodField()
    class Meta:
        model=Laptop
        fields=["brand" , "name" , "price" , "image" , "memory" , "processor" , "storage_type" , "release_date","seller"]
    
    def get_images(self,obj):
        images=obj.images.all()
        return UploadImageLaptopSerializer(instance=images , many=True).data
