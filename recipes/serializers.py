from rest_framework import serializers

from .models import Recipe, Tag


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("title", "author", "short_description", "calories_per_serving", "difficulty", "tags",)

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("name",)