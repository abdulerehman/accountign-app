from django.db import models
from uuid import uuid4


class VendorType(models.Model):
    type = models.CharField(max_length=255)


class CategoryType(models.Model):
    type = models.CharField(max_length=255)


class Vendors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, blank=True, unique=True)
    vendortypes = models.ForeignKey(VendorType, on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    phone_1 = models.CharField(max_length=15)
    phone_2 = models.CharField(max_length=15, blank=True, null=True)
    email_1 = models.EmailField()
    email_2 = models.EmailField(blank=True, null=True)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, blank=True, unique=True)
    categorytype_id = models.ForeignKey(CategoryType, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    external_account_no = models.CharField(max_length=255)
    default_category = models.BooleanField(default=False)
    system_category = models.BooleanField(default=False)
    sub_account_of = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

class Bill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, blank=True, unique=True)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=255)
    invoice_date = models.DateField()
    date_due = models.DateField()
    bill_memo = models.TextField()
    paid_in_full = models.BooleanField(default=False)
    Reference = models.CharField(max_length=255)
    Sub_total = models.DecimalField(max_digits=10, decimal_places=2)

class BillItems(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, blank=True, unique=True)
    bills_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    memo = models.TextField()
    vendor_credit_id = models.IntegerField()  # Assuming vendor_credit_id is an integer
    Reference = models.CharField(max_length=255)

class Checks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, blank=True, unique=True)
    bankaccount_id = models.IntegerField()  # Assuming bankaccount_id is an integer
    check_no = models.CharField(max_length=255)
    check_cut_date = models.DateField()
    check_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vendor_id = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    print_date = models.DateField()
    check_memo = models.TextField()
    Reference = models.CharField(max_length=255)
