from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.debug import sensitive_post_parameters

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "homepage/index.html",
    )


@sensitive_post_parameters()
def register(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, f"Account für {username} erstellt!")
            return redirect("login")
    else:
        form = UserCreationForm()
    context = {"form": form}
    return render(request, "homepage/register.html", context)
