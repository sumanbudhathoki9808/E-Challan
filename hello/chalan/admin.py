from django.contrib import admin

# Register your models here.


from .models import HomeImage, challan, contact, dynamicAbout

admin.site.register(challan)
admin.site.register(dynamicAbout)
admin.site.register(contact)
admin.site.register(HomeImage)