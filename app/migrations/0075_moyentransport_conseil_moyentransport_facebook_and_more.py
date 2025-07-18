# Generated by Django 4.2.21 on 2025-07-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0074_rename_acces_lieu_adresse_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moyentransport',
            name='conseil',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='moyentransport',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moyentransport',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='moyentransport',
            name='services',
            field=models.TextField(blank=True, help_text='Services et équipements disponibles', null=True),
        ),
        migrations.AddField(
            model_name='moyentransport',
            name='zone_desservi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
