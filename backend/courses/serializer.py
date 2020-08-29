from rest_framework.serializers import ModelSerializer

from .models import Courses


class CourseSerializer(ModelSerializer):
    """Добавление курсов"""
    class Meta:
        model = Courses
        fields = ['id', 'name', 'url', 'rating']
