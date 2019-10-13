from django.urls import include, path
from django_recipe.cooking_recipes import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"ingredients", views.IngredientViewSet)
router.register(r"ingredientamounts", views.IngredientAmountViewSet)
router.register(r"recipes", views.RecipeViewSet)

app_name = "cooking_recipes"
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
