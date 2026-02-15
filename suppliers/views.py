from rest_framework import viewsets
from .models import Supplier
from .serializers import SupplierSerializer
from django.shortcuts import render,redirect
from django.contrib import messages
from materials.models import Materials

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
    def supplier_register(request):
        materials = Materials.objects.all()
        if request.method == 'POST':
            company_name=request.POST['company_name']
            email=request.POST['email']
            phone=request.POST['phone']
            current_location=request.POST['current_location']
            latitude=request.POST['latitude']
            altitude=request.POST['altitude']
            gst_number=request.POST['gst_number']
            bank_account=request.POST['bank_account']
            ifsc=request.POST['ifsc']
            upload_document = request.FILES.get('documents')
            materials_supplied=request.POST.getlist['list_of_material']
            supplier = Supplier.objects.create(
                company_name=company_name,
                email=email,
                phone=phone,
                current_location=current_location,
                latitude=latitude,
                altitude=altitude,
                gst_number=gst_number,
                bank_account=bank_account,
                ifsc=ifsc,
                documents=upload_document)
            supplier.list_of_material.set(materials_supplied)
            print('Supplier Created')
            return redirect('home')
        else:
            return render(request, "supplier_register.html", {"materials": materials})
            
      
