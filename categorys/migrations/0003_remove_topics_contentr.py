# Generated by Django 4.2.5 on 2023-09-15 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorys', '0002_topics_contentr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='contentr',
        ),
    ]
