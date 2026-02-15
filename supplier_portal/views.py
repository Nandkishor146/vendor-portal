from django.shortcuts import render,redirect
from materials.models import Materials
from suppliers.models import Supplier

def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')


def supplier_register(request):
        materials = Materials.objects.all()
        if request.method == 'POST':
            company_name=request.POST['company_name']
            phone=request.POST['phone']
            current_location=request.POST['current_location']
            latitude=request.POST['latitude']
            altitude=request.POST['altitude']
            gst_number=request.POST['gst_number']
            bank_account=request.POST['bank_account']
            ifsc=request.POST['ifsc']
            aadhar = request.FILES.get('document1')
            pan = request.FILES.get('document2')
            gst_certificate = request.FILES.get('document3')
            materials_supplied=request.POST.getlist('list_of_material')
            supplier = Supplier.objects.create(
                company_name=company_name,
                phone=phone,
                current_location=current_location,
                latitude=latitude,
                altitude=altitude,
                gst_number=gst_number,
                bank_account=bank_account,
                ifsc=ifsc,
                aadhar=aadhar,
                pan=pan,
                gst_certificate=gst_certificate)
            supplier.list_of_material.set(materials_supplied)
            print('Supplier Created')
            return redirect('base')
        else:
            return render(request, "supplier_register.html", {"materials": materials})
            