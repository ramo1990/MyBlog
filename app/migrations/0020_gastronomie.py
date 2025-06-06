# Generated by Django 4.2.21 on 2025-05-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_delete_gastronomie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gastronomie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='gastronomie_images/')),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
