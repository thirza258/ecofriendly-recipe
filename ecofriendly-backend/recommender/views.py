from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.
class RecommenderView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'message': 'Welcome to the Recommender System!'
        }
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        # Handle POST request here
        data = {
            'message': 'POST request received!'
        }
        return JsonResponse(data)