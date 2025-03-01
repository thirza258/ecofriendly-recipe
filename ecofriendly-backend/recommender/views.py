from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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