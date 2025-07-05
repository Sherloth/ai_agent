import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        # Convert to absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if the file path is within the working directory
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        result = subprocess.run(
            ["python", abs_file_path],
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
            timeout=30
        )

        parts = []

        # Collect stdout and stderr
        if result.stdout.strip():
            parts.append("STDOUT:\n" + result.stdout.strip())
        if result.stderr.strip():
            parts.append("STDERR:\n" + result.stderr.strip())

        # Add exit code if non-zero
        if result.returncode != 0:
            parts.append(f"Process exited with code {result.returncode}")

        return "\n\n".join(parts) if parts else "No output produced."

    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out after 30 seconds'

    except Exception as e:
        return f"Error: executing Python file: {e}"
