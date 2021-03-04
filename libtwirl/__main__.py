from libtwirl.errors import IncorrectArgumentFormatError
from libtwirl.core.install import pkg_install
from libtwirl.core.remove import pkg_remove
from sys import argv

args = argv[1:]
pkgs = args[1:]

# List of actions
operations = {
	"install": pkg_install,
	"remove": pkg_remove,
	"purge": None,
	"search": None
}

# Check for argument errors
if not operations[args[0]]:
	raise IncorrectArgumentFormatError(f"Unknown operation '{args[0]}'. Valid operations are {', '.join(operations.keys())}.")
if not len(args) > 1:
	raise IncorrectArgumentFormatError("No packages specified.")

# Do operations
operations[args[0]](pkgs)

