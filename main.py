import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv


def main():
    # Check if a prompt is provided
    if len(sys.argv) < 2:
        print("Error: No prompt provided.\nUsage: python3 main.py \"<your prompt here>\"")
        sys.exit(1)
    
    # Adding flag
    verbose_flag = False
    arguments = []

    for arg in sys.argv[1:]:
        if arg == "--verbose":
            verbose_flag = True
        else:
            arguments.append(arg)

    # Load environment variables from .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment.")
        sys.exit(1)

    # Configure the genai client with API key
    genai.configure(api_key=api_key)

    # Initialize model
    model = genai.GenerativeModel("gemini-1.5-flash") # can use pro here

    prompt = " ".join(arguments)

    # Create list of content messages
    messages = [
        {"role": "user", "parts": [prompt]}
    ]

    response = model.generate_content(messages)
    
    

    # Print token usage if available
    if verbose_flag:
        print(f"User prompt: {prompt}")
        if hasattr(response, 'usage_metadata'):
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
        else:
            print("Token usage information not available.")
    

    # Print the generated text
    print(response.text)

if __name__ == "__main__":
    main()
