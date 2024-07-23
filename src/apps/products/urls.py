from rest_framework import routers
from .views import *

router=routers.SimpleRouter()

router.register(r'phones',PhoneViewSet)
router.register(r'laptops',LaptopViewSet)

urlpatterns = []+router.urls
