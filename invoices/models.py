from django.db import models
from suppliers.models import Supplier
from django.utils import timezone

class Invoice(models.Model):
    Status_choices=[
         ('PENDING', 'Pending Verification'),
         ('APPROVED', 'Approved')
     ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,related_name='invoices')
    invoice_number = models.CharField(max_length=50,unique=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=50,choices=Status_choices, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if not self.invoice_number:
            year = timezone.now().year
            last_invoice = Invoice.objects.filter(
                invoice_number__startswith=f"INV-{year}"
            ).order_by('id').last()

            if last_invoice:
                last_number = int(last_invoice.invoice_number.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1

            self.invoice_number = f"INV-{year}-{new_number:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number