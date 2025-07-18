import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

FUNCTION_REGISTRY = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(function_call_part, verbose=False):
    call_function_name = function_call_part.name
    args = dict(function_call_part.args)
    args["working_directory"] = os.path.abspath("./calculator")

    if verbose:
        print(f"Calling function: {call_function_name}({args})")
    else:
        print(f"- Calling function: {call_function_name}")

    target_function = FUNCTION_REGISTRY.get(call_function_name)
    if not target_function:
        return {
            "role": "tool",
            "parts": [
                {
                    "function_response": {
                        "name": call_function_name,
                        "response": {
                            "error": f"Unknown function: {call_function_name}"
                        }
                    }
                }
            ]
        }

    try:
        function_result = target_function(**args)
    except Exception as e:
        function_result = f"Function raised an exception: {str(e)}"

    return {
        "role": "tool",
        "parts": [
            {
                "function_response": {
                    "name": call_function_name,
                    "response": {"result": function_result}
                }
            }
        ]
    }
