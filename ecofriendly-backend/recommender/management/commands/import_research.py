import os
import pandas as pd
from django.core.management.base import BaseCommand
from recommender.models import RecipeModel

class Command(BaseCommand):
    help = "Import recipe data from a CSV file"

    def handle(self, *args, **kwargs):
        # Get the absolute path of the script
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Correct path to the CSV file
        file_path = os.path.join(base_dir, "data", "recipes.csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        dataset = pd.read_csv(file_path) 

        for _, row in dataset.iterrows():
            RecipeModel.objects.create(
                title=row["title"],
                ingredients=row["ingredients"],
                instructions=row["method"],
                url=row["url"]
            )
            
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))
