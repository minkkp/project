# Generated by Django 3.2.16 on 2023-04-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_area',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_living',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
