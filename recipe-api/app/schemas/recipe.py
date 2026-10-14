from pydantic import BaseModel

class Recipe(BaseModel):
    title: str
    cuisine: str
    prep_time: int
    servings: int
