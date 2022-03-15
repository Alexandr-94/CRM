from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'country', 'address')


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'patronymic', 'last_name', 'date_of_birth', 'level', 'skills')


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('languages',)

