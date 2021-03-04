from libtwirl.errors import IncorrectArgumentFormatError
from libtwirl.core.install import pkg_install
from sys import argv

args = argv[1:]

flags = [
    "install",
    "remove",
    "purge", 
    "search"
]

count = 0
try:
    for arg in args: 
        if args[count] not in flags and count != 1:
            raise IncorrectArgumentFormatError(f"Unknown argument '{args[count]}'. (Valid arguments are {', '.join(flags)})")
        count += 1
    if count != 2:
        raise IncorrectArgumentFormatError(f"Incorrect amount of operations provided. (Expected 2, got {count})")
except Exception as E:
    raise SystemExit()
pkg_install(argv[2])
