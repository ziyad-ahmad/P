# Generated by Django 4.2.3 on 2023-07-12 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='auther',
            new_name='authers',
        ),
       
    ]
