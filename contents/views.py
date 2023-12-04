from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from contents.models import Content
from contents.serializers import ContentSerializer
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminOrAuthenticated, IsCourseStudentOwner
from django.shortcuts import get_object_or_404
from courses.models import Course
from drf_spectacular.utils import extend_schema


@extend_schema(
          tags= ['Criação de conteúdo']
  )

class ContentView(CreateAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAdminOrAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = "course_id"

    def perform_create(self, serializer):
        found_course = get_object_or_404(Course, pk=self.kwargs.get("course_id"))
        return serializer.save(course=found_course)

@extend_schema(
          tags= ['Listagem, edição e exclusão de conteúdo']
  )


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes =[JWTAuthentication]
    permission_classes = [IsAdminOrAuthenticated, IsCourseStudentOwner]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    

    def get_object(self):
        try:
            print(self.kwargs.get('course_id'))
            Course.objects.get(id=self.kwargs.get("course_id"))
            content = Content.objects.get(id=self.kwargs.get("content_id"))
        except Course.DoesNotExist:
            error = {"detail": "course not found."}
            raise NotFound(error)
        except Content.DoesNotExist:
            error = {"detail": "content not found."}
            raise NotFound(error)
        self.check_object_permissions(self.request, content)
        return content
    
   
