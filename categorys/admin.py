from django.contrib import admin
from .models import Category, MainTopic, Topics
# Register your models here.


admin.site.register(Category)
admin.site.register(MainTopic)
admin.site.register(Topics)