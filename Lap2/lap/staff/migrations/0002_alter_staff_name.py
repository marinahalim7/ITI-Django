# Generated by Django 4.2 on 2023-04-23 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
