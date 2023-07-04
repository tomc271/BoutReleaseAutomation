from pathlib import Path
import re


def get_full_filepath(filepath):

    return Path(r"C:\git\BOUT-dev") / filepath


def update_version_number_in_file(full_filepath, pattern, new_version_number):

    with open(full_filepath, "r", encoding='UTF-8') as file:
        file_contents = file.read()
        updated_text = re.sub(pattern, new_version_number, file_contents)

    with open(full_filepath, "w", encoding='UTF-8') as file:
        file.write(updated_text)


def bump_version_numbers():

    new_version_number = "6.1.2"
    short_version_number = "6.1"
    bout_next_version_number = "6.2.0"

    update_version_number_in_file(
        get_full_filepath("configure.ac"), r"(?<=AC_INIT\(\[BOUT\+\+\],\[)\d\.\d\.\d(?=\])", new_version_number)

    update_version_number_in_file(
        get_full_filepath("CITATION.cff"), r"(?<=version: )\d\.\d\.\d", new_version_number)

    update_version_number_in_file(
        get_full_filepath("manual/sphinx/conf.py"), r"(?<=version = \")\d\.\d(?=\")", short_version_number)

    update_version_number_in_file(
        get_full_filepath("manual/sphinx/conf.py"), r"(?<=release = \")\d\.\d\.\d(?=\")", new_version_number)

    update_version_number_in_file(
        get_full_filepath("manual/doxygen/Doxyfile_readthedocs"), r"(?<=PROJECT_NUMBER         = )\d\.\d\.\d",
        new_version_number)

    update_version_number_in_file(
        get_full_filepath("manual/doxygen/Doxyfile"), r"(?<=PROJECT_NUMBER         = )\d\.\d\.\d", new_version_number)

    update_version_number_in_file(
        get_full_filepath("CMakeLists.txt"), r"(?<=set\(_bout_previous_version \"v)\d\.\d\.\d(?=\"\))",
        new_version_number)

    update_version_number_in_file(
        get_full_filepath("CMakeLists.txt"), r"(?<=set\(_bout_next_version \")\d\.\d\.\d(?=\"\))",
        bout_next_version_number)

    update_version_number_in_file(
        get_full_filepath("tools/pylib/_boutpp_build/backend.py"), r"(?<=_bout_previous_version = \"v)\d\.\d\.\d(?=\")",
        new_version_number)

    update_version_number_in_file(
        get_full_filepath("tools/pylib/_boutpp_build/backend.py"), r"(?<=_bout_next_version = \"v)\d\.\d\.\d(?=\")",
        bout_next_version_number)


if __name__ == '__main__':

    bump_version_numbers()
