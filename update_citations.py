from pathlib import Path
import yaml

authors_from_git = ["A Allen", "Aaron Fisher", "Adam Dempsey", "Andrew Allen", "arkabokshi", "Ben Dudson", "bendudson",
                    "Benjamin Dudson", "Brendan", "Brendan Shanahan", "Brett Friedman", "brey", "BS", "bshanahan",
                    "Chenhao Ma", "Chris MacMackin", "D Dickinson", "David", "David Bold", "David Dickinson",
                    "David Schwörer", "dependabot[bot]", "Dmitry Feliksovich Meyerson", "Dmitry Meyerson", "dschwoerer",
                    "Eric Medwedeff", "Erik Grinaker", "Fabio Riva", "George Breyiannis", "GitHub Merge Button",
                    "github-actions[bot]", "hahahasan", "Haruki Seto", "Haruki SETO", "holger", "Holger Jones",
                    "Hong Zhang", "Ilon Joseph", "Ilon Joseph - x31405", "Jarrod Leddy", "JB Leddy", "j-b-o",
                    "Jed Brown", "Jens Madsen", "John Omotani", "johnomotani", "jonesholger", "Joseph Parker",
                    "Joshua Sauppe", "Kab Seok Kang", "kangkabseok", "Kevin Savage", "Licheng Wang", "loeiten",
                    "Luke Easy", "M Leconte", "M V Umansky", "Marta Estarellas", "Matt Thomas", "Maxim Umansky",
                    "Maxim Umansky - x26041", "Michael Løiten", "Michael Loiten Magnussen", "Minwoo Kim",
                    "Nicholas Walkden", "Nick Walkden", "nick-walkden", "Olivier Izacard", "Pengwei Xi", "Peter Hill",
                    "Peter Naylor", "Qin, Yining", "Sajidah Ahmed", "Sanat Tiwari", "Sean Farley", "seanfarley",
                    "Seto Haruki", "Simon Myers", "Tianyang Xia", "Toby James", "tomc271", "Tongnyeol Rhee",
                    "Xiang Liu", "Xinliang Xu", "Xueqiao Xu", "Yining Qin", "ZedThree", "Zhanhui Wang"]


def parse_cff_file(filename):
    with open(filename, "r", encoding='UTF-8') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


def get_authors_from_cff_file():
    filename = Path(r"C:\git\BOUT-dev") / "CITATION.cff"
    file_contents = parse_cff_file(filename)
    try:
        return file_contents["authors"]
    except KeyError as key_error:
        print("Failed to find section:", key_error, "in", filename)


def author_found_in_existing_authors(author, existing_authors):

    existing_author_names = [(a.get("given-names"), a.get("family-names")) for a in existing_authors]

    try:
        given_names, surname = author.split()
        matches = [n for n in existing_author_names if n[1].casefold() == surname.casefold()]
        for match in matches:
            if match[0].casefold() == given_names.casefold():  # The given name also matches
                return True
            if match[0][0].casefold() == given_names[0].casefold():  # The first initial also matches
                return True

    except ValueError as value_error:  # Only a single name, so could not split()

        if value_error.args[0] == "not enough values to unpack (expected 2, got 1)":

            surname_matches = [n for n in existing_author_names if n[1].casefold() == author.casefold()]
            if len(surname_matches) > 0:
                return True

            given_name_matches = [n for n in existing_author_names if n[0].casefold() == author.casefold()]
            if len(given_name_matches) > 0:
                return True

            combined_name_matches = [n for n in existing_author_names if
                                     (n[0] + n[1]).casefold() == author.casefold()]
            if len(combined_name_matches) > 0:
                return True

    return False


def update_citations():
    existing_authors = get_authors_from_cff_file()
    for author in authors_from_git:
        if not author_found_in_existing_authors(author, existing_authors):
            print(author, "not found. Add to citations?")


if __name__ == '__main__':
    update_citations()
