from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),

    # URL pattern for including URLs from the "subjects" app
    path("", include("subjects.urls")),
]
