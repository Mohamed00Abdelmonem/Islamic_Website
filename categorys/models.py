from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.contrib.auth.models import User  # Assuming you are using Django's built-in User model

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, verbose_name=_("Author"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class MainTopic(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(null=True,blank=True, max_length=255, verbose_name=_("Subtitle"))
    content = models.TextField(null=True,blank=True,verbose_name=_("Content"))
    tags = TaggableManager(verbose_name=_("Tags"))
    created_at = models.DateTimeField(default=timezone.now, verbose_name=_("Created At"))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, verbose_name=_("Author"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Category"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Main Topic")
        verbose_name_plural = _("Main Topics")

class Topics(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    subtitle = models.CharField(max_length=255, verbose_name=_("Subtitle"))
    content = models.TextField(verbose_name=_("Content"))
    tags = TaggableManager(verbose_name=_("Tags"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True, verbose_name=_("Author"))
    maintopic = models.ForeignKey(MainTopic, on_delete=models.CASCADE, verbose_name=_("Main Topic"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Topic")
        verbose_name_plural = _("Topics")
