from django.contrib import admin
from blog.models import Tag, Post,Comment
# Register your models here.



admin.site.register(Tag)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display=['title','slug','published_at']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display=['creator','created_at']
