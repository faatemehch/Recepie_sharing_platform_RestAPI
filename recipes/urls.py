from django.urls import path, include

from .views import RecipeViewSet, TagViewSet, CustomerViewSet, CommentViewSet

from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("recipes", RecipeViewSet, basename="recipes")
router.register("tags", TagViewSet, basename="tags")
router.register('customers', CustomerViewSet, basename='customer')

recipe_routers = routers.NestedDefaultRouter(router, 'recipes', lookup='recipe')
recipe_routers.register('comments', CommentViewSet, basename='recipe-comments')


urlpatterns = router.urls + recipe_routers.urls