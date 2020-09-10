from django.contrib import admin

from .models import BookRecord, Genre


admin.site.register(BookRecord)
admin.site.register(Genre)
