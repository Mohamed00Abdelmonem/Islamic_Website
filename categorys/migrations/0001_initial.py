# Generated by Django 4.2.5 on 2023-09-15 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MainTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subtitle')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created At')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorys.category', verbose_name='Category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Main Topic',
                'verbose_name_plural': 'Main Topics',
            },
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('content', models.TextField(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('maintopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorys.maintopic', verbose_name='Main Topic')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Topic',
                'verbose_name_plural': 'Topics',
            },
        ),
    ]