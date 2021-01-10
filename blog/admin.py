from django.contrib import admin
from .models import Post

# to make the model visible on the admin page, we need to register it
admin.site.register(Post)
