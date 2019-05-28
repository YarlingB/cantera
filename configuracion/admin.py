from django.contrib import admin
from .models import *

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
	fieldsets = [
        ('Slider 1',{'fields':['texto_1','foto_1','credito_1']}),
        ('Slider 2',{'fields':['texto_2','foto_2','credito_2']}),
        ('Slider 3',{'fields':['texto_3','foto_3','credito_3']}),
        ]

admin.site.register(SiteConfiguration)
admin.site.register(Slider,SliderAdmin)