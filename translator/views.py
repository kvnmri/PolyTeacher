from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer
import google.generativeai as genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
print(f"GEMINI_API_KEY: {api_key}")
genai.configure(api_key=api_key)

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        print(os.environ.get("GEMINI_API_KEY"))
        text_to_translate = request.query_params.get("text", None)
        
        if not text_to_translate:
            return Response(
                {"error": "Le paramètre 'text' est requis."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            response = genai.generate_text(
                model="models/text-bison-001",
                prompt=(f"Traduis ce texte en espagnol : {text_to_translate}. Affiche uniquement la traduction.")
            )
            
            return Response({"translation": response.result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class FrenchItalianTranslationViewSet(APIView):

    def get(self, request):

        data = Translation.objects.all()
        serialized_data = TranslationSerializer(data, many=True)

        return Response(data=serialized_data.data, status=None)

class AllTranslation(APIView):

    def get(self, request):

        data = Translation.objects.all() # select * from translation
        serialized_data = TranslationSerializer(data, many=True) # formattage des données

        return Response(data=serialized_data.data, status=None) # affichage des données sous forme de réponse

def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})