from django.contrib import admin

from publications.models import Publication, Comments

# Register your models here.
admin.site.register(Publication)
admin.site.register(Comments)