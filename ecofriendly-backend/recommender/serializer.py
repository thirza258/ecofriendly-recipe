from .models import RecipeModel
from rest_framework import serializers

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = "__all__"