# Generated by Django 3.1.7 on 2021-05-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chalan', '0004_auto_20210511_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernames', models.CharField(max_length=200)),
                ('phonenumbers', models.IntegerField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('descs', models.TextField()),
            ],
        ),
    ]