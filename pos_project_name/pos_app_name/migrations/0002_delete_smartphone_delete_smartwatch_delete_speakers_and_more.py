# Generated by Django 4.1.7 on 2023-04-25 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos_app_name', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Smartphone',
        ),
        migrations.DeleteModel(
            name='SmartWatch',
        ),
        migrations.DeleteModel(
            name='Speakers',
        ),
        migrations.DeleteModel(
            name='TV',
        ),
    ]