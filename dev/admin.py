from django.contrib import admin
from .models import metadata, metrics
# Register your models here.
admin.site.register(metadata)
admin.site.register(metrics)