from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all().order_by("-created_at")
    return render(request, "projects/project_list.html", {"projects": projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/project_detail.html", {"project": project})

@login_required
def add_project(request):
    if request.method == "POST":
        # Include request.FILES to handle image/video uploads
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            project.collaborators.add(request.user)  # auto-join creator
            form.save_m2m()  # save collaborators if any
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/add_project.html", {"form": form})
