# Generated by Django 2.2.4 on 2020-12-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showsapp', '0003_auto_20201214_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(verbose_name='%m/%d/%Y'),
        ),
    ]