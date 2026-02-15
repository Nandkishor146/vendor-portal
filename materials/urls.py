from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaterialsViewSet

router = DefaultRouter()
router.register(r'add',MaterialsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
