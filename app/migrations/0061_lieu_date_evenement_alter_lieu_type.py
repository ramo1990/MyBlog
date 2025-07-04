# Generated by Django 4.2.21 on 2025-06-27 10:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_tag_lieu_region_lieu_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='lieu',
            name='date_evenement',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lieu',
            name='type',
            field=models.CharField(choices=[('nature', 'Nature'), ('culture', 'Culture'), ('plage', 'Plage'), ('gastronomie', 'Gastronomie'), ('village', 'Village'), ('randonnee', 'Randonnee'), ('animaux', 'Animaux'), ('bar', 'Bar'), ('club', 'Club'), ('concert', 'Concert'), ('spectacle', 'Spectacle'), ('evenement', 'Événement')], max_length=100),
        ),
    ]
