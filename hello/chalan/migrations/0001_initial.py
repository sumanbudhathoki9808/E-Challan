# Generated by Django 3.2 on 2021-05-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='challan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=200)),
                ('phonenumber', models.IntegerField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('licensenumber', models.IntegerField(max_length=200)),
                ('vehiclenumber', models.CharField(max_length=200)),
                ('vehicletype', models.CharField(max_length=200)),
                ('creator', models.CharField(max_length=200)),
            ],
        ),
    ]