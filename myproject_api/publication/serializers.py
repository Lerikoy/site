from rest_framework import serializers
from .models import BlogPost, PostTour

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        lookup_field = 'slug'

class PostTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTour
        fields = '__all__'
        lookup_field = 'slug'

class PublicationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['user', 'title', 'category', 'image', 'content']
