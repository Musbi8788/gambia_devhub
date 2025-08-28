from django.urls import path
from . import views

urlpatterns = [
    path("", views.dev_list, name="dev_list"),
    path("<int:profile_id>/", views.dev_detail, name="dev_detail"),
]
