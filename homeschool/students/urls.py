from django.urls import path

from . import views

app_name = "students"
urlpatterns = [
    path("", views.StudentIndexView.as_view(), name="index"),
    path("create/", views.StudentCreateView.as_view(), name="create"),
    path(
        "<uuid:uuid>/courses/<uuid:course_uuid>/",
        views.StudentCourseView.as_view(),
        name="course",
    ),
    path("grade/", views.GradeView.as_view(), name="grade"),
    path(
        "<uuid:uuid>/enroll/<uuid:school_year_uuid>/",
        views.EnrollmentCreateView.as_view(),
        name="enrollment_create",
    ),
]
