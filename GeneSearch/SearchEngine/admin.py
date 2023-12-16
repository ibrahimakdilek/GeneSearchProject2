from django.contrib import admin

# Register your models here.
from .models import GeneList


class GeneStudyAdmin(admin.ModelAdmin):
    list_display= ('approved_symbol' ,'previous_symbol', 'synonyms')
    search_fields= ('approved_symbol' ,'previous_symbol', 'synonyms' )

admin.site.register(GeneList,GeneStudyAdmin)
