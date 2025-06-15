import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

def main():
    # Check if a prompt is provided
    if len(sys.argv) < 2:
        print("Error: No prompt provided.\nUsage: python3 main.py \"<your prompt here>\"")
        sys.exit(1)

    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment.")
        sys.exit(1)

    # Configure the genai client with API key
    genai.configure(api_key=api_key)

    # Initialize model
    model = genai.GenerativeModel("gemini-1.5-flash")  # Replace with "gemini-1.5-pro" if needed

    # Generate content
    prompt = " ".join(sys.argv[1:])
    response = model.generate_content(prompt)

    # Print token usage if available
    if hasattr(response, 'usage_metadata'):
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    else:
        print("Token usage information not available.")

    # Print the generated text
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
