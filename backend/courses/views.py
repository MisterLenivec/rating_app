from rest_framework.viewsets import ModelViewSet

from .models import Courses
from .serializer import CourseSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
