from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Recipe, Tag
from .serializers import RecipeSerializer, TagSerializer

class RecipeViewSet(ModelViewSet):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.filter(is_active=True, is_public=True)
    permission_classes = [IsAuthenticated]



