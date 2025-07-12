import os
import sys
import json
import google.generativeai as genai
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from google.generativeai import types

def main():
    if len(sys.argv) < 2:
        print("Error: No prompt provided.\nUsage: python3 main.py \"<your prompt here>\"")
        sys.exit(1)

    # Handle --verbose flag
    verbose_flag = False
    arguments = []
    for arg in sys.argv[1:]:
        if arg == "--verbose":
            verbose_flag = True
        else:
            arguments.append(arg)

    # Load API key from .env
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment.")
        sys.exit(1)

    genai.configure(api_key=api_key)

    # Register function tools
    available_functions = types.Tool(function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file
    ])

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        tools=[available_functions],
    )

    # Build prompt
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file content
    - Execute Python files
    - Write to a file

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    prompt = " ".join(arguments)
    combined_prompt = f"{system_prompt.strip()}\n\n{prompt.strip()}"

    # Generate response
    try:
        response = model.generate_content(
            combined_prompt,
            generation_config=genai.types.GenerationConfig(),
        )
    except Exception as e:
        print(f"Error: Failed to generate response: {e}")
        sys.exit(1)

    # Verbose logging
    if verbose_flag:
        print(f"User prompt: {prompt}")
        if hasattr(response, 'usage_metadata'):
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
        print("Full response object:\n", response)

    # Handle response
    function_call_handled = False

    if response.candidates:
        for candidate in response.candidates:
            if candidate.content.parts:
                for part in candidate.content.parts:
                    # Detect function call robustly
                    fn_call = getattr(part, "function_call", None)
                    if not fn_call and hasattr(part, "_proto") and part._proto.WhichOneof("data") == "function_call":
                        fn_call = part._proto.function_call

                    if fn_call:
                        fn_name = fn_call.name
                        fn_args_raw = fn_call.args
                        print(f"📞 Function call detected:\nName: {fn_name}\nArgs: {fn_args_raw}")

                        try:
                            args = dict(fn_args_raw)
                            if fn_name == "get_files_info":
                                from functions.get_files_info import get_files_info
                                result = get_files_info(working_directory=os.getcwd(), **args)
                                print("get_files_info() executed successfully!")
                                print(json.dumps(result, indent=2))
                                function_call_handled = True

                            elif fn_name == "get_file_content":
                                from functions.get_file_content import get_file_content
                                result = get_file_content(working_directory=os.getcwd(), **args)
                                print("get_file_content() executed successfully!")
                                print(json.dumps(result, indent=2))
                                function_call_handled = True

                            elif fn_name == "run_python_file":
                                from functions.run_python_file import run_python_file
                                result = run_python_file(working_directory=os.getcwd(), **args)
                                print("run_python_file() executed successfully!")
                                print(result)
                                function_call_handled = True

                            elif fn_name == "write_file":
                                from functions.write_file import write_file
                                result = write_file(working_directory=os.getcwd(), **args)
                                print("write_file() executed successfully!")
                                print(json.dumps(result, indent=2) if isinstance(result, dict) else result)
                                function_call_handled = True

                        except Exception as e:
                            print("Error during function execution:", e)
                        break
            if function_call_handled:
                break

        if not function_call_handled:
            print("No function call handled. Attempting to print text response:")
            for candidate in response.candidates:
                if candidate.content.parts:
                    for part in candidate.content.parts:
                        if hasattr(part, "text"):
                            print(part.text)
                        elif isinstance(part, str):
                            print(part)
    else:
        print("❗ No response candidates received.")

if __name__ == "__main__":
    main()
