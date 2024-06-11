from django.contrib import admin
from .models import Counter, Tasks


# Register your models here.


admin.site.register(Counter)
admin.site.register(Tasks)