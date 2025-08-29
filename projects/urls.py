from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("<int:project_id>/", views.project_detail, name="project_detail"),
    path("add/", views.add_project, name="add_project"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)