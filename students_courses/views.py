
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from students_courses.models import StudentCourse
from students_courses.serializers import StudentCourseSerializer
from courses.models import Course
from accounts.models import Account
from rest_framework.views import Response, status
from accounts.permissions import IsAdminOrAuthenticated
from drf_spectacular.utils import extend_schema


@extend_schema(
          tags= ['Inclusão e listagem de estudantes em um curso']
  )


class StudentCourseView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrAuthenticated]
    queryset = Course.objects.all()
    serializer_class = StudentCourseSerializer
    lookup_url_kwarg="course_id"

    
    def update(self, request, *args, **kwargs):
        found_course = self.get_object() 
        request_data = request.data.get('students_courses',[])
        email_list = []

        for request_student in request_data:
            student_email = request_student.get('student_email')
            if student_email:
                try:
                    student = Account.objects.get(email=student_email)
                except Account.DoesNotExist:
                    email_list.append(student_email)
                    continue

                if not StudentCourse.objects.filter(course=found_course, student=student).exists():
                    student_course = StudentCourse(course=found_course, student=student)
                    student_course.save()
            
        
        if email_list:
            error_message = (
                f'No active accounts was found: {", ".join(email_list)}.'
            )
            return Response({'detail':error_message}, status=status.HTTP_400_BAD_REQUEST)
        serializer = StudentCourseSerializer(found_course)
        return Response(serializer.data, status=status.HTTP_200_OK)

      
      
   