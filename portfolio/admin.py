from django.contrib import admin
from .models import Port
# Register your models here.
admin.site.site_header="ADMIN SITE"
admin.site.site_title="ADMIN SITE"
admin.site.register(Port)