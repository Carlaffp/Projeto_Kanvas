from rest_framework import serializers
from students_courses.models import StudentCourse
from courses.models import Course



class StudentsCoursesSerializer(serializers.ModelSerializer):
    student_id = serializers.CharField(read_only=True, source='student.id')
    student_email = serializers.CharField(read_only=True, source='student.email')
    student_username = serializers.CharField(read_only=True, source='student.username')
    class Meta:
        model = StudentCourse
        fields = ['id', 'student_id', 'student_username','student_email','status']
        extra_kwargs = {'id':{'read_only':True}}


class StudentCourseSerializer(serializers.ModelSerializer):
   
    students_courses = StudentsCoursesSerializer(many=True, read_only=True)
    name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'students_courses']
        extra_kwargs = {'id':{'read_only':True}}
        depth = 1

