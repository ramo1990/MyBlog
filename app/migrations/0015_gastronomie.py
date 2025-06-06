# Generated by Django 4.2.21 on 2025-05-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_agenda_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gastronomie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='gastro_images/')),
                ('lieu', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
