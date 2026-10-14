from fastapi import FastAPI

from app.config import APP_NAME, APP_VERSION
from app.routers.recipe import router as recipes_router
from app.routers.ingredients import router as ingredients_router


app = FastAPI(
    title = APP_NAME,
    version = APP_VERSION

)


app.include_router(recipes_router)
app.include_router(ingredients_router)


@app.get("/")
def read_root():
    return {"message": "This is my Recipe API"}