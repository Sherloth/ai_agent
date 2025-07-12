import os
from google.generativeai import types
from pprint import pprint

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters={
        "type": "object",
        "properties": {
            "directory": {
                "type": "string",
                "description": (
                    "The directory to list files from, relative to the working directory. "
                    "If not provided, lists files in the working directory itself."
                ),
            }
        },
        "required": [],
    }
)

def get_files_info(working_directory, directory=None):
    try:
        base = os.path.abspath(working_directory)
        if directory:
            target = os.path.abspath(os.path.join(base, directory))
        else:
            target = base

        if not target.startswith(base):
            return { "error": f"Cannot list '{directory}' as it is outside the permitted working directory" }

        if not os.path.exists(target):
            return { "error": f"'{directory}' does not exist" }
        if not os.path.isdir(target):
            return { "error": f"'{directory}' is not a directory" }

        entries = []
        for entry_name in os.listdir(target):
            entry_path = os.path.join(target, entry_name)
            try:
                if os.path.isdir(entry_path):
                    is_dir = True
                    file_size = 0
                elif os.path.isfile(entry_path):
                    is_dir = False
                    file_size = os.path.getsize(entry_path)
                else:
                    is_dir = False
                    file_size = 0

                entries.append({
                    "name": entry_name,
                    "size_bytes": file_size,
                    "is_dir": is_dir
                })
            except Exception as e:
                entries.append({
                    "name": entry_name,
                    "error": str(e)
                })

        result = {
        'directory': directory if directory else ".",
        'files': entries
        }
        pprint(result)
        return result

    except Exception as e:
        return { 'error': str(e) }
