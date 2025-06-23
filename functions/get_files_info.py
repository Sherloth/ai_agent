import os

def get_files_info(working_directory, directory=None):
    try:
        base = os.path.abspath(working_directory)
        if directory:
            target = os.path.abspath(os.path.join(base, directory))
        else:
            target = base

        if not target.startswith(base):
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

        if not os.path.exists(target):
            return f"Error: '{directory}' does not exist"
        if not os.path.isdir(target):
            return f"Error: '{directory}' is not a directory"

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

                entries.append(f"- {entry_name}: file_size={file_size} bytes, is_dir={is_dir}")
            except Exception as e:
                entries.append(f"- {entry_name}: Error retrieving entry info: {e}")

        return "\n".join(entries)

    except Exception as e:
        return f"Error: {e}"
