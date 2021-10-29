from rest_framework import serializers
from .models import Article, Type


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name', 'color']


class ArticleSerializer(serializers.ModelSerializer):
    type = TypeSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'short_description', 'description', 'type']


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'short_description', 'description', 'type']


class ArticleByTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'short_description', 'description', 'type']
