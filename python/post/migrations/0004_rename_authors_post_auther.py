# Generated by Django 4.2.3 on 2023-07-12 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_rename_authers_post_authors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authors',
            new_name='auther',
        ),
    ]
