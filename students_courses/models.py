from django.db import models
import uuid


class StudentCourseStatus(models.TextChoices):
    PENDING = "pending"
    ACCEPTED = "accepted"


class StudentCourse(models.Model):
  student = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="students_courses")
  course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="students_courses")
  id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
  status = models.CharField(
     choices=StudentCourseStatus.choices,
     default=StudentCourseStatus.PENDING
  )
