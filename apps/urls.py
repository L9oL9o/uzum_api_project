from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ProductModelViewSet, UserModelViewSet, SellerModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('user', UserModelViewSet, 'user')
router.register('seller', SellerModelViewSet, 'seller')

urlpatterns = [
    path('router-url/', include(router.urls)),
]
