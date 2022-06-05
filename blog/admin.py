from django.contrib import admin
from .models import Post

# All models that admin can access
admin.site.register(Post)
