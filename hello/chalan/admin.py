from django.contrib import admin

# Register your models here.


from .models import challan, contact, dynamicAbout

admin.site.register(challan)
admin.site.register(dynamicAbout)
admin.site.register(contact)