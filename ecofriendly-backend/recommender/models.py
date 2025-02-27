from django.db import models
from pydantic import BaseModel, Field
from typing import List

# Create your models here.
class RecipeModel(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    url = models.URLField()
    
    def __str__(self):
        return self.title
    
class RecipeReturnModel(BaseModel):
    title: str = Field(..., description="Recipe Title")
    ingredients: str = Field(..., description="Ingredients")
    instructions: str = Field(..., description="Instructions")
    url: str = Field(..., description="URL")
    
class RecipeListReturnModel(BaseModel):
    recipes: List[RecipeReturnModel] = Field(..., description="List of Recipes")
    response: str = Field(..., description="Response Message")