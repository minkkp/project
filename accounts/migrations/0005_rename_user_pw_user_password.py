# Generated by Django 3.2.18 on 2023-04-13 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230413_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_pw',
            new_name='password',
        ),
    ]
