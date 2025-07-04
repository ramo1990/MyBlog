# Generated by Django 4.2.21 on 2025-06-24 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_alter_culture_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/')),
            ],
        ),
        migrations.RemoveField(
            model_name='culture',
            name='categorie',
        ),
        migrations.RemoveField(
            model_name='cultureimage',
            name='culture',
        ),
        migrations.DeleteModel(
            name='CategorieCulture',
        ),
        migrations.DeleteModel(
            name='Culture',
        ),
        migrations.DeleteModel(
            name='CultureImage',
        ),
    ]
