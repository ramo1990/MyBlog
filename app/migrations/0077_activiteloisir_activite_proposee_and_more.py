# Generated by Django 4.2.21 on 2025-07-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_restaurant_conseil_restaurant_specialite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activiteloisir',
            name='activite_proposee',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='activiteloisir',
            name='categorie',
            field=models.CharField(choices=[('parc', 'Parc'), ('sport', 'Activité sportive'), ('centre_loisir', 'Centre de loisirs'), ('jeux', 'Jeux pour enfants'), ('cinema', 'Cinema'), ('autre', 'Autre')], max_length=50),
        ),
    ]
