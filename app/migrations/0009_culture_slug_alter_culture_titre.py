# Generated by Django 4.2.21 on 2025-05-17 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_conseilvoyage_contenu'),
    ]

    operations = [
        migrations.AddField(
            model_name='culture',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='culture',
            name='titre',
            field=models.CharField(max_length=200),
        ),
    ]
