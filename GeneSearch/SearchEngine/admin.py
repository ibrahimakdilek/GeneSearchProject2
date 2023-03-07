from django.contrib import admin

# Register your models here.
from .models import GeneList


class GeneStudyAdmin(admin.ModelAdmin):
    list_display= ('approved_symbol', 'date_name_changed' ,'previous_symbol', 'synonyms', 'linked_genes')
    search_fields= ('approved_symbol', 'date_name_changed' ,'previous_symbol', 'synonyms', 'linked_genes')

admin.site.register(GeneList,GeneStudyAdmin)
