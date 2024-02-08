from django.contrib import admin
from.models import *
# Register your models here.

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'link')
   
@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    list_display = ('count_students', 'count_university', 'year_of_experienced', 'count_countries')


@admin.register(Servic)
class ServicAdmin(admin.ModelAdmin):
    list_display = ('title', 'discription', 'icon', 'order')

@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('image', 'name', 'name_institute', 'degree')


@admin.register(contakt)
class contaktAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'choice_institution', 'telefon_number','message')

@admin.register(review)
class reviewAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'name')

@admin.register(social)
class socialAdmin(admin.ModelAdmin):
    list_display = ('icon', 'order', 'link')

















