from django_recipe.cooking_recipes.models import Recipe, Ingredient, IngredientAmount
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="cooking_recipes:ingredient-detail"
    )

    class Meta:
        model = Ingredient
        fields = ["url", "name"]


class IngredientAmountSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="cooking_recipes:ingredientamount-detail"
    )
    name = serializers.ReadOnlyField(source="ingredient.name")

    class Meta:
        model = IngredientAmount
        fields = ["url", "name", "amount", "unit", "ingredient", "recipe"]


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="cooking_recipes:recipe-detail"
    )
    ingredients = IngredientAmountSerializer(
        source="ingredientamount_set", many=True, read_only=True
    )

    class Meta:
        model = Recipe
        fields = ["url", "title", "description", "ingredients"]
