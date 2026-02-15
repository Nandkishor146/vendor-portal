from django.db import models
from materials.models import Materials
class Supplier(models.Model):
     Status_choices=[
         ('PENDING', 'Pending Verification'),
         ('APPROVED', 'Approved'),
         ('REJECTED', 'Rejected')
         ]
     company_name = models.CharField(max_length=200)
     phone = models.CharField(max_length=15)
     current_location=models.CharField(max_length=50,null=True,blank=True)
     latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
     altitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
     list_of_material=models.ManyToManyField(Materials)
     gst_number = models.CharField(max_length=20)
     bank_account = models.CharField(max_length=50,null=True, blank=True)
     ifsc = models.CharField(max_length=20,null=True, blank=True)
     aadhar= models.FileField(upload_to='supplier_docs/', blank=True, null=True)
     pan= models.FileField(upload_to='supplier_docs/', blank=True, null=True)
     gst_certificate= models.FileField(upload_to='supplier_docs/', blank=True, null=True)
     status = models.CharField(max_length=20, choices=Status_choices, default='PENDING')
     is_approved = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True)
    
     def __str__(self):
        return self.company_name
