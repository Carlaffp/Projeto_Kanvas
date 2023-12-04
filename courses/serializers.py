from rest_framework import serializers
from courses.models import Course
from contents.serializers import ContentSerializer
from students_courses.serializers import StudentCourseSerializer



class CourseSerializer(serializers.ModelSerializer):
    students_courses = StudentCourseSerializer(many=True, read_only=True, source="students")
    contents = ContentSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id','name', 'status','start_date', 'end_date', 'instructor', 'students_courses', 'contents']
    
