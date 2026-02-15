from rest_framework import serializers
from .models import Supplier
from django import forms
from materials.models import Materials

class SupplierSerializer(serializers.ModelSerializer):
    list_of_material = serializers.PrimaryKeyRelatedField(many=True,queryset=Materials.objects.all())
    class Meta:
        model = Supplier
        exclude = ['status', 'is_approved', 'created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔥 THIS LINE loads materials into UI
        self.fields['list_of_material'].queryset = Materials.objects.all() 