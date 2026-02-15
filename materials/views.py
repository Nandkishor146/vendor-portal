from rest_framework import viewsets
from .models import Materials
from .serializers import MaterialsSerializer

class MaterialsViewSet(viewsets.ModelViewSet):
    queryset =Materials.objects.all()
    serializer_class = MaterialsSerializer
