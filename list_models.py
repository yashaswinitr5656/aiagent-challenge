import google.generativeai as genai

# Configure API key
genai.configure(api_key="AIzaSyDkWl5c4regaWj_Wm6TP0THNPXl9X61uww")

# List models
for model in genai.list_models():
    print(model.name)
