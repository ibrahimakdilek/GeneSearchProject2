# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class GeneList(models.Model):
    approved_symbol = models.TextField(db_column='approved_symbol', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    previous_symbol = models.TextField(db_column='previous_symbol', blank=True, null=True)  # Field name made lowercase.
    synonyms = models.TextField(db_column='synonyms', blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'gene_fin'

    


