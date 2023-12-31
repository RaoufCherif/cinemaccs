"""cinemaccs_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cinemaccs_project import settings
from cinemaccs_project.views import (
    BrandViewSet,
    TheaterViewSet,
    TheaterPictureViewSet,
    RoomViewSet,
    RoomPictureViewSet,
    DescriptionElementViewSet
)
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"brands", BrandViewSet, basename="brand")
router.register(
    r"delems", DescriptionElementViewSet, basename="descriptionelement"
)
router.register(r"theaters", TheaterViewSet, basename="theater")
router.register(
    r"theaterspic", TheaterPictureViewSet, basename="theaterpicture"
)
router.register(r"rooms", RoomViewSet, basename="room")
router.register(r"roomspic", RoomPictureViewSet, basename="roompicture")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
