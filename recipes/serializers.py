from django.utils.text import slugify

from rest_framework import serializers

from .models import Recipe, Tag, Comment, Customer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("recipe", "author", "name", "text",)


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("user", "phone_number", "birth_date",)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name",)

# ---------------------------- Recipe ----------------------------
class RecipeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'short_description', 'ingredients','instructions', 'calories_per_serving')


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'short_description', 'ingredients','instructions', 'calories_per_serving')



class RecipeSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = Recipe
        fields = ("id", "title", "slug", "author", "short_description", "ingredients", "calories_per_serving",
                  "difficulty", "tags")
        read_only_fields = ("slug", "author",)

    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        recipe = Recipe(**validated_data)
        recipe.slug = slugify(recipe.title)
        recipe.save()
        recipe.tags.set(tags)
        return recipe
