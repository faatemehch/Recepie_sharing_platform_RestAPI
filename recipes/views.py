from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Recipe, Tag, Customer, Comment
from .serializers import (
    RecipeSerializer,
    RecipeCreateSerializer,
    RecipeUpdateSerializer,
    TagSerializer,
    CustomerSerializer,
    CommentSerializer
)


class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.filter(is_active=True, is_public=True)
    http_method_names = ('get', 'post', 'patch', 'delete', 'option', 'head')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreateSerializer
        if self.request.method == 'PATCH':
            return  RecipeUpdateSerializer
        if self.request.user.is_staff:
            return RecipeSerializer
        return RecipeSerializer


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    # permission_classes = [IsAuthenticated]


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        user_id = request.user.id
        customer = Customer.objects.get(id=user_id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
