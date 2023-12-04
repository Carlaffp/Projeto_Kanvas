from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminOrAuthenticated
from drf_spectacular.utils import extend_schema


@extend_schema(
          tags= ['Criação e Listagem de cursos']
  )

class CourseView(ListCreateAPIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAdminOrAuthenticated]
  queryset = Course.objects.all()
  serializer_class = CourseSerializer


  def get_queryset(self) -> Course:
        if self.request.user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(students=self.request.user.id)


@extend_schema(
          tags= ['Listagem , edição e exclusão de curso']
  )

class CourseDetailView(RetrieveUpdateDestroyAPIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAdminOrAuthenticated]
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
  lookup_url_kwarg= "course_id"

  def get_queryset(self) -> Course:
        print(self.request.user)
        if self.request.user.is_superuser:
            return Course.objects.all()
        return Course.objects.filter(students=self.request.user.id)


