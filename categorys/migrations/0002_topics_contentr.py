# Generated by Django 4.2.5 on 2023-09-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='contentr',
            field=models.TextField(default=' ', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
