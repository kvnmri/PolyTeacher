import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
prompt = input("Entrez votre prompt : ")
# prompt = "écrire le prompt"

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)
print(response.text)