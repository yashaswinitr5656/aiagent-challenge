import argparse
import os
import google.generativeai as genai

# Configure Gemini API
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # load variables from .env file
api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise RuntimeError("GENAI_API_KEY not set in .env file")
genai.configure(api_key=api_key)


def call_llm(prompt: str) -> str:
    # Choose a supported model
    model = genai.GenerativeModel("models/gemini-2.5-pro")
    
    # Generate content
    response = model.generate_content(prompt)
    
    # Return the text from the response
    return response.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agent-as-Coder CLI")
    parser.add_argument("--target", required=True, help="Target bank name (e.g., icici)")
    args = parser.parse_args()
    target = args.target.lower()

    print("Target:", target)

    # Create custom_parsers folder if it doesn't exist
    os.makedirs("custom_parsers", exist_ok=True)

    # Prompt for the LLM
    prompt = f"Write a Python parser for {target} bank statement. The parser should extract data and save it to a CSV file."

    # Call LLM
    code_text = call_llm(prompt)

    # Save generated code to a file
    parser_file = f"custom_parsers/{target}_parser.py"
    with open(parser_file, "w", encoding="utf-8") as f:
        f.write(code_text)

    print(f"Parser saved to {parser_file}")
    print("Generated Code Preview:\n")
    print(code_text[:500])  # preview first 500 chars


