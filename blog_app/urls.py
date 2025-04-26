from django.urls import include, path

from .views import *

app_name = "blog_app"
urlpatterns = [
    path("", index_view, name="index"),
    path("create/", create_post_view, name="create_post"),
    path("edit/<int:post_id>/", edit_post_view, name="edit_post"),
    path("<int:post_id>/", post_view, name="post_detail"),
]
