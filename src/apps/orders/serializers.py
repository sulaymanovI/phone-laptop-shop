from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Order
        fields="__all__"
    
    def create(self, validated_data):
        
        phone_orders_data=validated_data.pop('phone_orders')
        laptop_orders_data=validated_data.pop('laptop_orders')
        order=Order.objects.create(**validated_data)

        for phone_order_data in phone_orders_data:
            PhoneOrder.objects.create(order=order , **phone_order_data)
        
        for laptop_order_data in laptop_orders_data:
            LaptopOrder.objects.create(order=order , **laptop_order_data)
        
        return order

class PhoneOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=PhoneOrder
        fields="__all__"

class LaptopOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=LaptopOrder
        fields="__all__"
