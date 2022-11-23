from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("applications.home.urls")),
    path("", include("applications.users.urls")),
    path("", include("applications.flujos.urls")),
]
# handling the 404 error
handler404 = "applications.errors.views.handler_404"