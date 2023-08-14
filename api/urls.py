from django.urls import include, path

from .router import urlpatterns

urlpatterns = [
    path(r"", include(urlpatterns)),
]
