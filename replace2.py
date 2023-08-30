import sys
import re

"""
    Replaces all found matches of <partern> by the replace <string> on the file <filename>
    <pattern> is a RegExp
"""


def main():
    filename = sys.argv[1]
    pattern = sys.argv[2]
    string = sys.argv[3]

    with open(filename, "r") as f:
        data = f.read()

    data = re.sub(
        pattern=rf"{pattern}",
        repl=rf"{string}",
        string=data,
    )

    with open(filename, "w") as f:
        f.write(data)


if __name__ == "__main__":
    main()
