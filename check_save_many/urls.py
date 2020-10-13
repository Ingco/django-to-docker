from django.urls import path, include

from rest_framework.routers import SimpleRouter

from . import apis


api_router = SimpleRouter()
api_router.register(
    r"parent",
    apis.ParentViewSet,
    basename="parent"
)
api_router.register(
    r"child",
    apis.ChildViewSet,
    basename="child"
)

# app_name = "check_save_many"
urlpatterns = [
    path("", include(api_router.urls), name="check_api"),
]
