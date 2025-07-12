import os
from google.generativeai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file (within the working directory) with a limit of 10,000 characters.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": (
                    "Path to the file to be read, relative to the working directory."
                ),
            }
        },
        "required": ["file_path"],
    }
)

def get_file_content(working_directory, file_path):
    try:
        # Convert to absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the file path is within the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if it's a regular file
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file contents
        with open(abs_file_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        # Truncate if necessary
        if len(content) > 10000:
            return content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'

        return content

    except Exception as e:
        return f"Error: {str(e)}"
