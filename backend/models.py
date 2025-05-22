from pydantic import BaseModel, Field
from typing import List

class Ingredient(BaseModel):
    """
    Use this model when representing a single ingredient in a recipe.
    """
    name: str = Field(description="Name of the ingredient")
    amount: float = Field(description="Quantity of the ingredient needed")
    unit: str = Field(description="Unit of measurement (e.g., cups, grams, pieces)")

class Recipe(BaseModel):
    """
    Use this model when working with complete cooking recipes.
    """
    title: str = Field(title="title", description="Name of the recipe")
    ingredients: List[Ingredient] = Field(title="ingredients", description="List of ingredients needed for the recipe")
    instructions: List[str] = Field(title="instructions", description="Step-by-step instructions to prepare the recipe")

class RecipeDoc(BaseModel):
    """
    Use this model when you have multiple recipes that you need to put into the doc
    """
    recipes: List[Recipe] = Field(description="a list of recipes")