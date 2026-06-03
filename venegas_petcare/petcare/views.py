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
    
class Vacunas(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        mascotas = request.data.get("mascotas", [])

        for mascota in mascotas:
            nombre = mascota.get("nombre")
            peso_kg = mascota.get("peso_kg")

        total_cobro= 0
        detalle = []
        
        for mascota in mascotas:
            nombre = mascota.get("nombre")
            peso_kg = mascota.get("peso_kg")

            if peso_kg < 5:
                costo = 10
            elif 5 <= peso_kg <= 20:
                costo = 20
            else:
                costo = 30

            total_cobro += costo
            detalle.append({"nombre": nombre, "costo": costo})