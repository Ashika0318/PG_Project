# Generated by Django 4.0.7 on 2024-03-22 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scientist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirement',
            name='leaf_type',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='sampletype',
        ),
        migrations.RemoveField(
            model_name='requirement',
            name='tree_height',
        ),
    ]