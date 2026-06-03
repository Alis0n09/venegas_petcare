from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EspeciesViewSet, MascotasViewSet

router = DefaultRouter()
router.register(r"especies", EspeciesViewSet, basename="especies")
router.register(r"mascotas", MascotasViewSet, basename="mascotas")

urlpatterns = []
urlpatterns += router.urls