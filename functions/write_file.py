import os
from google.generativeai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file within the working directory. Overwrites existing files or creates new ones.",
    parameters={
        "type": "object",
        "properties": {
            "file_path": {
                "type": "string",
                "description": "Relative path to the file where content should be written."
            },
            "content": {
                "type": "string",
                "description": "The text content to write into the file."
            }
        },
        "required": ["file_path", "content"],
    }
)

def write_file(working_directory, file_path, content):
    try:
        # Convert to absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the file path is within the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        # Ensure parent directories exist
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)

        # Write the content (overwrite mode)
        with open(abs_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return {
            "file_path": file_path,
            "content": content,
            "status": f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        }
    except Exception as e:
        return f"Error: {str(e)}"