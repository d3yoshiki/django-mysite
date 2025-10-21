from django.contrib import admin
from .models import Question  # もしくはPolicy

admin.site.register(Question)
