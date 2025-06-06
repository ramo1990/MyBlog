# Generated by Django 4.2.21 on 2025-05-26 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='agenda_images/')),
                ('lieu', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
