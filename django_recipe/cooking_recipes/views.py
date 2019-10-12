from rest_framework import viewsets
from django_recipe.cooking_recipes.models import Ingredient, Recipe, IngredientAmount
from django_recipe.cooking_recipes.serializers import (
    IngredientSerializer,
    RecipeSerializer,
    IngredientAmountSerializer,
)


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited.
    """

    queryset = Ingredient.objects.all().order_by("name")
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """

    queryset = Recipe.objects.all().order_by("title")
    serializer_class = RecipeSerializer


class IngredientAmountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows IngredientAmounts to be viewed or edited.
    """

    queryset = IngredientAmount.objects.all()
    serializer_class = IngredientAmountSerializer
