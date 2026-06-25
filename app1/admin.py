from django.contrib import admin
from .models import *
from .views import studentreg

# Register your models here.
admin.site.register(logindata)
admin.site.register(admindata)
admin.site.register(Student)
admin.site.register(Cardata)
admin.site.register(userdata)
admin.site.register(carphotos)
admin.site.register(AddToCart)
admin.site.register(BookNow)
admin.site.register(Payment)