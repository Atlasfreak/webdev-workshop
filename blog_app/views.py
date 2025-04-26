from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import CommentForm, PostForm
from .models import Post

# Create your views here.


def index_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, "blog_app/index.html", context)


@login_required
def create_post_view(request: HttpRequest) -> HttpResponse:
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post: Post = form.save(commit=False)
            post.author = request.user
            post.save()

    return render(request, "blog_app/create_post.html", {"form": form})


@login_required
def edit_post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    if post.author != request.user:
        return HttpResponse("Unauthorized", status=401)

    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post erfolgreich bearbeitet!")
            return redirect("blog_app:post_detail", post_id=post.id)

    return render(request, "blog_app/edit_post.html", {"form": form})


def post_view(request: HttpRequest, post_id: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    if not request.user.is_authenticated:
        comment_form = None
    else:
        comment_form = CommentForm()
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()

    context = {
        "post": post,
        "comment_form": comment_form,
        "is_creator": post.author == request.user,
    }
    return render(request, "blog_app/post.html", context)
