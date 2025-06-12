import os
from dotenv import load_dotenv
from google import genai

def main():
    # Load API key from the .env file
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create the Gemini client
    client = genai.Client(api_key=api_key)

    # Send a prompt to the model
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

    # Print the result
    print(response.text)

    # Print token usage
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
# Making sure code only run when executed directly
if __name__ == "__main__":
    main()