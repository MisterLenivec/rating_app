from rest_framework.viewsets import ModelViewSet

from .models import Courses
from .serializer import CourseSerializer


class CoursesViewSet(ModelViewSet):
    """Вывод списка курсов"""
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
