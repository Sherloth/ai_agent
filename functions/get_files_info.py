from pathlib import Path

def get_files_info(working_directory, directory=None):
    base = Path(working_directory).resolve()
    target = Path(directory or base).resolve()

    # Check if target is within the working directory
    try:
        target.relative_to(base)
    except ValueError:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # Check if target exists and is a directory
    if not target.exists() or not target.is_dir():
        return f'Error: "{directory}" is not a directory'

    # Build directory listing
    entries = []
    for entry in target.iterdir():
        file_size = entry.stat().st_size
        is_dir = entry.is_dir()
        entries.append(f"- {entry.name}: file_size={file_size} bytes, is_dir={is_dir}")

    return "\n".join(entries)
# adding entry for boot to check