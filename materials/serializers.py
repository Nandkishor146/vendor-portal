from rest_framework import serializers
from .models import Materials

class MaterialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materials
        fields='__all__'