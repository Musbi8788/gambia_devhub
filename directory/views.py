from django.shortcuts import render, get_object_or_404
from accounts.models import Profile

def dev_list(request):
    query = request.GET.get("q")
    if query:
        developers = Profile.objects.filter(skills__icontains=query)
    else:
        developers = Profile.objects.all()
    return render(request, "directory/dev_list.html", {"developers": developers})

def dev_detail(request, profile_id):
    developer = get_object_or_404(Profile, id=profile_id)
    return render(request, "directory/dev_detail.html", {"developer": developer})
