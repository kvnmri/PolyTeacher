import requests

api_key = "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" # To complete
model = "gpt-4o-mini"
prompt = input("Prompt : ")
hearders = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
parameters= {
    "model": model,
    "prompt": prompt,
    "max_tokens": 100
}
response = requests.post(f"https://api.openai.com/v1/completions", headers=hearders, json=parameters).json()
print(response)