from django.urls import path, include

from .views import RecipeViewSet, TagViewSet

from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("recipes", RecipeViewSet, basename="recipes")
router.register("tags", TagViewSet, basename="tags")

recipe_routers = routers.NestedDefaultRouter(router, 'recipes', lookup='recipe')
tags_routers = routers.NestedDefaultRouter(router, 'tags', lookup='tag')

urlpatterns = router.urls + recipe_routers.urls + tags_routers.urls