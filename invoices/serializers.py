from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Invoice
        exclude = ['status']
        read_only_fields=['invoice_number']