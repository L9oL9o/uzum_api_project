from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ProductModelViewSet, UserModelViewSet, SellerModelViewSet, CatalogModelViewSet, \
    CategoryModelViewSet, TypeModelViewSet, OrderModelViewSet, DiscountModelViewSet

router = DefaultRouter()
router.register('catalog', CatalogModelViewSet, 'catalog')
router.register('category', CategoryModelViewSet, 'category')
router.register('type', TypeModelViewSet, 'type')
router.register('user', UserModelViewSet, 'user')
router.register('product', ProductModelViewSet, 'product')
router.register('seller', SellerModelViewSet, 'seller')
router.register('orders', OrderModelViewSet, 'orders')
router.register('discount', DiscountModelViewSet, 'discount')

urlpatterns = [
    path('router-url/', include(router.urls)),
]

