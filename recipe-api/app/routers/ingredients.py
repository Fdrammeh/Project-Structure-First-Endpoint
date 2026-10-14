from fastapi import APIRouter
from app.schemas.ingredient import Ingredient


router = APIRouter(prefix="/ingredients", tags=["Ingredients"])


ingredients = [
    {
        "id": 1,
        "name": "Chicken",
        "category": "Protein"
    },
    {
        "id": 2,
        "name": "Tomato",
        "category": "Vegetable"
    }
]


@router.get("/")
def get_ingredients():
    return ingredients


@router.post("/")
def create_ingredient(ingredient: Ingredient):
    new_ingredient = {
        "id": len(ingredients) + 1,
        **ingredient.model_dump()
    }

    ingredients.append(new_ingredient)

    return new_ingredient