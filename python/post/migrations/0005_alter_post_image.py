# Generated by Django 4.2.3 on 2023-07-12 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_rename_authors_post_auther'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='Posts'),
        ),
    ]
