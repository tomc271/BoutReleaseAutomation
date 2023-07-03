from pathlib import Path
import re


def get_filepath(filepath):

    return Path(r"C:\git\BOUT-dev") / filepath


def update_version_number_in_files(new_version_number):

    filepath = get_filepath("configure.ac")
    with open(filepath, "r", encoding='UTF-8') as file:
        file_contents = file.read()

        pattern = r"AC_INIT\(\[BOUT\+\+\],\[(\d\.\d\.\d)\]"
        replacement = "AC_INIT([BOUT++],[" + new_version_number + "]"
        updated_text = re.sub(pattern, replacement, file_contents)
    with open(filepath, "w", encoding='UTF-8') as file:
        file.write(updated_text)


if __name__ == '__main__':

    update_version_number_in_files("6.1.2")
