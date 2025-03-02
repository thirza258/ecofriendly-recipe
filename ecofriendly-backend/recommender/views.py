from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import json
from langchain_core.output_parsers import JsonOutputParser
from rest_framework.generics import ListAPIView
from .models import RecipeModel, RecipeListReturnModel, RecipeReturnModel
from .serializer import RecipeSerializer
from .main import rag_index

class GetAllRecipe(ListAPIView):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    
class RecommendationSystem(APIView):
    def post(self, request):
        try:
            input_prompt = request.data.get('input_prompt')
            llm = init_chat_model("gpt-4o-mini", model_provider="openai")
            retrieved_data = rag_index.retrieve_documents(input_prompt, k=3)
            
            context = "\n\n".join([
                f"Title: {json.loads(doc)['title']}\nIngredients: {json.loads(doc)['ingredients']}\n"
                f"Instructions: {json.loads(doc)['instructions']}\nURL: {json.loads(doc)['url']}"
                for doc in retrieved_data
            ])
            parser = JsonOutputParser(pydantic_object=RecipeListReturnModel)
            
            prompt = PromptTemplate(
                template="""
                You are an AI assistant using retrieved data about eco-friendly recipes to answer user queries.  
                You have access to a list of eco-friendly recipes.  
                Use the provided research results to enhance your response.  

                Retrieved Research Documents:  
                {context}  

                User Query:  
                {query}  

                Format your response as a JSON object matching this schema:  
                {format_instructions}  

                Ensure that:  
                - Each ingredient is **delimited by ";"** in the output.  
                - Each step of the instruction is **delimited by ";"** in the output.  
                - Maintain accuracy and clarity while formatting the response.  

                """,
                input_variables=["query", "context"],
                partial_variables={"format_instructions": parser.get_format_instructions()},
            )
            chain = prompt | llm | parser
            response = chain.invoke({"query": input_prompt, "context": context})
            return Response({
                "status": 200,
                "message": "Success",
                "data": response
                }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response({
                "error": str(e),
                "status": 400,
                }, status=status.HTTP_400_BAD_REQUEST)