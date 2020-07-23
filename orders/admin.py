from django.contrib import admin

# Register your models here.
from .models import Fooditem,Catergory,Extras,Order,Top,Cart,Size

admin.site.register(Fooditem)
admin.site.register(Catergory)
admin.site.register(Extras)
admin.site.register(Order)
admin.site.register(Top)
admin.site.register(Cart)
admin.site.register(Size)
