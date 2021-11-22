from django.contrib import admin

# Register your models here.
from .models import saleMedicineApp

admin.site.site_header = "Sale System"
class saleMedicineAdmin (admin.ModelAdmin):
	list_display = ['customer_name','customer_phone']

admin.site.register(saleMedicineApp,saleMedicineAdmin)
