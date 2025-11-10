from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Mood Recipe Recommendation API")

# Data models
class Mood(BaseModel):
    id: int
    name: str

class Recipe(BaseModel):
    id: int
    name: str
    ingredients: List[str]
    instructions: str
    moods: List[int]  # Related mood ids

# Sample in-memory data
moods = [
    Mood(id=1, name="Happy"),
    Mood(id=2, name="Sad"),
    Mood(id=3, name="Energetic")
]

recipes = [
    Recipe(id=1, name="Chocolate Cake", ingredients=["flour", "sugar", "cocoa"], instructions="Mix and bake.", moods=[1,2]),
    Recipe(id=2, name="Fruit Smoothie", ingredients=["banana", "berries"], instructions="Blend all.", moods=[3])
]

# API endpoints
@app.get("/api/moods", response_model=List[Mood])
def get_moods():
    return moods

class RecommendationRequest(BaseModel):
    mood_id: int

@app.post("/api/recommendations", response_model=List[Recipe])
def get_recommendations(req: RecommendationRequest):
    matched = [r for r in recipes if req.mood_id in r.moods]
    if not matched:
        raise HTTPException(status_code=404, detail="No recipes found for given mood")
    return matched

@app.get("/api/recipes/{recipe_id}", response_model=Recipe)
def get_recipe(recipe_id: int):
    for r in recipes:
        if r.id == recipe_id:
            return r
    raise HTTPException(status_code=404, detail="Recipe not found")
