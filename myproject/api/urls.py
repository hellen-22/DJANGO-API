from django.urls import path, include
from . views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("blog", BlogViewSet, basename="blog")
router.register("announcement", AnnouncementViewSet, basename="announcement")
router.register("suggestion", SuggestionViewSet, basename="suggestion")
router.register("school", SchoolViewSet, basename="school")
router.register("department", DepartmentViewSet, basename="department")
router.register("course", CourseViewSet, basename="course")
router.register("student", StudentViewSet, basename="student")
router.register("lecturer", LecturerViewSet, basename="lecturer")

urlpatterns = [
    path("", include(router.urls)),
]