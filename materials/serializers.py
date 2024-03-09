from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lessons_amount = serializers.SerializerMethodField()

    @staticmethod
    def get_lessons_amount(obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['name', 'preview', 'description', 'lessons', 'lessons_amount']
