# Generated by Django 4.1 on 2022-08-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneList',
            fields=[
                ('approved_symbol', models.TextField(blank=True, db_column='Approved_Symbol', primary_key=True, serialize=False)),
                ('date_name_changed', models.TextField(blank=True, db_column='Date_Name_Changed', null=True)),
                ('previous_symbol', models.TextField(blank=True, db_column='Previous_Symbol', null=True)),
                ('synonyms', models.TextField(blank=True, db_column='Synonyms', null=True)),
                ('linked_genes', models.TextField(blank=True, db_column='Linked_Genes', null=True)),
            ],
            options={
                'db_table': 'Gene_List',
                'managed': False,
            },
        ),
    ]
