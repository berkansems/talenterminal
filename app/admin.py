from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from app.models import *
# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name','email','position','application_date',)
    list_filter = ('position',)
    search_fields = ('email',)
admin.site.register(Clients, ClientsAdmin)

class DevelopersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'english_level', 'specialization', 'experience', 'application_date',)
    list_filter = ('english_level', 'specialization', 'experience', 'skills',)
    search_fields = ('email',)
admin.site.register(Developers,DevelopersAdmin)
