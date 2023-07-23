from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import CustomSignUpForm, CustomLoginForm
from .models import Project


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomLoginForm(request=request)
    return render(request, "login.html", {"form": form})


def sign_up_view(request):
    if request.method == "POST":
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomSignUpForm()
    return render(request, "signup.html", {"form": form})


@login_required
def index_view(request):
    user = request.user
    projects = user.projects.all()
    return render(request, "home.html", context={"projects": projects})


@login_required
def new_project_view(request):
    if request.method == "POST":
        project_name = request.POST.get("project_name", "New Project")
        user = request.user
        project = Project.objects.create(
            name=project_name,
            user=user,
            number_of_rooms=2,
            input_data_json="",
            output_data_json="",
        )
        return redirect("project_detail", project_id=project.pk)
    return render(request, "new_project.html")


@login_required
def project_view(request, project_id):
    user = request.user
    project = user.projects.filter(pk=project_id).first()
    return render(request, "project_detail.html", context={"project": project})


def pricing_view(request):
    return render(request, "pricing.html", context={"data": 13})
