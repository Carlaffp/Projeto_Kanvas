from django.urls import path
from courses.views import CourseView, CourseDetailView
from contents.views import ContentView, ContentDetailView
from students_courses.views import StudentCourseView

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<uuid:course_id>/", CourseDetailView.as_view()),
    path("courses/<uuid:course_id>/contents/", ContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/", ContentDetailView.as_view()),
    path("courses/<uuid:course_id>/students/",StudentCourseView.as_view())
]