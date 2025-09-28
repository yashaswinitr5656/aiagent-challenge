import google.generativeai as genai

load_dotenv()  # load variables from .env file
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise RuntimeError("GENAI_API_KEY not set in .env file")
genai.configure(api_key=api_key)

# List models
for model in genai.list_models():
    print(model.name)

