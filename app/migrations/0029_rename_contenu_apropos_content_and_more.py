# Generated by Django 4.2.21 on 2025-05-29 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_destinations_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apropos',
            old_name='contenu',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='apropos',
            old_name='titre',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='apropos',
            old_name='date_modifiee',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='gastronomie',
            old_name='description',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='gastronomie',
            old_name='date_pub',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='gastronomie',
            old_name='titre',
            new_name='title',
        ),
    ]
