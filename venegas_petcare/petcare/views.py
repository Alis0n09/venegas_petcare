from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Especies, Mascotas
from .serializers import EspeciesSerializer, MascotasSerializer
from .permissions import IsAdminOrReadOnly

class EspeciesViewSet(viewsets.ModelViewSet):                               #marcas = especie y vehiculos = mascota
    queryset = Especies.objects.all().order_by("id")
    serializer_class = EspeciesSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["nombre"]
    ordering_fields = ["id", "nombre"]

class MascotasViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.select_related("nombre").all().order_by("-id")
    serializer_class = MascotasSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["estado_vacunada"]
    search_fields = ["nombre__nombre", "chip"]
    ordering_fields = ["edad", "peso_kg"]

    def get_permissions(self):
        # Público: SOLO listar mascotas
        if self.action == "list":
            return [AllowAny()]
        return super().get_permissions()