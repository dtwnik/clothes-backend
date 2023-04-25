from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Men', MenViewSet)
router.register(r'Woman', WomanViewSet)
router.register(r'Kids', KidsViewSet)
router.register(r'Bestseller', BestsellerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', CustomObtainAuthToken.as_view()),
]
