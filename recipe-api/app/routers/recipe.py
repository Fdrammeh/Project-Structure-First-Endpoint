from fastapi import APIRouter
from app.schemas.recipe import Recipe

router = APIRouter(prefix="/recipes", tags=["Recipes"])

recipes = [
    {
        "id" : 2,
        "title":"Meat pie",
        "cuisine":"Jamaica",
        "prep_time_minutes":45,
        "servings":4

    },   

    {
        "id": 7,
        "title": "Pasta",
        "cuisine": "Italian",
        "prep_time_minutes": 45,
        "servings": 3
    }
]

@router.get("/")
def get_recipes():
    return recipes


@router.get("/{recipe_id}")
def get_recipe(recipe_id: int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe

    return {"error": "Recipe not found"}


@router.post("/")
def create_recipe(recipe: Recipe):
    new_recipe = {
        "id": len(recipes) + 1,
        **recipe.model_dump()
    }

    recipes.append(new_recipe)

    return new_recipe