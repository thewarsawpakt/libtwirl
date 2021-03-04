from libtwirl.errors import IncorrectArgumentFormatError
from libtwirl.core.install import pkg_install
from libtwirl.core.remove import pkg_remove
from sys import argv

# List of actions
operations = {
	"install": pkg_install,
	"remove": pkg_remove,
	"purge": None,
	"search": None
}

# Check for args
if not len(argv) > 1:
	raise IncorrectArgumentFormatError(f"No operation speficied. Valid operations are {', '.join(operations.keys())}.")

args = argv[1:]

# Check for argument errors
if not args[0] in operations.keys():
	raise IncorrectArgumentFormatError(f"Unknown operation '{args[0]}'. Valid operations are {', '.join(operations.keys())}.")
if not len(args) > 1:
	raise IncorrectArgumentFormatError("No packages specified.")

# Set pkgs after checks to avoid index out of range errors
pkgs = args[1:]
# Do operations
operations[args[0]](pkgs)
