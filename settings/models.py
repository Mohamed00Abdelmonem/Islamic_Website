from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    main_subtitle = models.TextField(max_length=500, null=True , blank=True)
    about_subtitle = models.TextField(max_length=500, null=True , blank=True)
    quran_subtitle = models.TextField(max_length=500, null=True , blank=True)
    prayer_subtitle = models.TextField(max_length=500, null=True , blank=True)
    awareness_subtitle = models.TextField(max_length=500, null=True , blank=True)
    ramdan_subtitle = models.TextField(max_length=500, null=True , blank=True)
    charity_and_donation_subtitle = models.TextField(max_length=500, null=True , blank=True)
    haij_subtitle = models.TextField(max_length=500, null=True , blank=True)
    shahadah_subtitle = models.TextField(max_length=500, null=True , blank=True)
    fasting_subtitle = models.TextField(max_length=500, null=True , blank=True)
    zakat_subtitle = models.TextField(max_length=500, null=True , blank=True)
    facbook_link = models.URLField(max_length=200 , null=True , blank=True)
    twitter_link = models.URLField(max_length=200 , null=True , blank=True)
    instgram_link = models.URLField(max_length=200 , null=True , blank=True)
    linkedin_link = models.URLField(max_length=200 , null=True , blank=True)
    phones = models.TextField(max_length=500, null=True , blank=True)
    email = models.TextField(max_length=500, null=True , blank=True)
    address = models.TextField(max_length=500, null=True , blank=True)
    android_app = models.URLField(max_length=200 , null=True , blank=True)
    ios_app = models.URLField(max_length=200 , null=True , blank=True)
    call_us = models.CharField(max_length=100 , null=True , blank=True)
    email_us = models.CharField(max_length=100 , null=True , blank=True)

    def __str__(self) -> str:
        return self.name