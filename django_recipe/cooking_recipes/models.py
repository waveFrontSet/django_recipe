from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient, through="IngredientAmount", through_fields=("recipe", "ingredient")
    )

    def __str__(self):
        return self.title


class IngredientAmount(models.Model):
    amount = models.FloatField()
    unit = models.CharField(max_length=20)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ingredient.name} {self.amount} {self.unit}"
