from django.contrib import admin
from .models import Vendors, VendorType, Category, CategoryType, Bill, BillItems, Checks


admin.site.register(Vendors)
admin.site.register(VendorType)
admin.site.register(Category)
admin.site.register(CategoryType)
admin.site.register(Bill)
admin.site.register(BillItems)
admin.site.register(Checks)