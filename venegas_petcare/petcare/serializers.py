from rest_framework import serializers
from .models import Especies, Mascotas

class EspeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especies
        fields = ["id", "nombre"]

class MascotasSerializer(serializers.ModelSerializer):
    nombre = serializers.PrimaryKeyRelatedField(queryset=Especies.objects.all())
    especie = serializers.CharField(source="nombre.nombre", read_only=True)
    total_mascotas = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Mascotas
        fields = ["id","nombre","especie","peso_kg","chip","edad","estado_vacunada","total_mascotas",]

    def get_total_mascotas(self, obj):
        if isinstance(obj, dict):
            return 0
        return obj.nombre.mascotas.count()