from rest_framework import serializers
from .models import Blog, Category

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.core.exceptions import ValidationError

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not value.endswith('@redberry.ge'):
            raise ValidationError("Email must be a Redberry domain email.")
        return value


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'text_color', 'background_color']

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(data='title', many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'image', 'publish_date', 'categories', 'author', 'email']
