from .serializers import *
from .permissions import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class PhoneViewSet(ModelViewSet):
    queryset=Phone.objects.all()
    serializer_class=PhoneSerializer
    permission_classes=[IsAuthenticated,IsSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class LaptopViewSet(ModelViewSet):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer
    permission_classes=[IsAuthenticated , IsSellerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
        print(self.request.user)