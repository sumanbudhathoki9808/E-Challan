# Generated by Django 3.1.7 on 2021-05-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chalan', '0003_auto_20210509_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challan',
            name='licensenumber',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='challan',
            name='phonenumber',
            field=models.CharField(max_length=200),
        ),
    ]