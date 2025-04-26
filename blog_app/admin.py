from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "creation_date",
        "edit_date",
        "text",
        "title",
    )
    list_filter = ("author", "creation_date", "edit_date")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "author", "creation_date", "text")
    list_filter = ("post", "author", "creation_date")
