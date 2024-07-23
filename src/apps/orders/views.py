from django.shortcuts import render
from .serializers import *
from .models import *
from .permissions import *
from rest_framework import generics , permissions

class OrderListCreateView(generics.ListCreateAPIView):
    
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated , IsOwnerOrReadOnly]

