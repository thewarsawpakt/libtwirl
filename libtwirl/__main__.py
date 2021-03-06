from libtwirl.errors import IncorrectArgumentFormatError
from libtwirl.core.database import register_repos
from libtwirl.core.install import pkg_install
from libtwirl.core.remove import pkg_remove
from pyalpm import Handle
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
try:
	handle = Handle(args[3], "/var/lib/pacman")
except:
	handle = Handle("/", "/var/lib/pacman")



# Register synced repositories automatically for now
# Preferred if a frontend does it themselves, see TODO below
# TODO: parse config to find repositories to register (or make the frontend handle it) instead of arbitrary repo list at end
# TODO: parse config and mirrorlist to find mirrors instead of arbitrary mirror
register_repos({
    "core": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"],
    "extra": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"],
    "community": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"]
    }, 
	handle=handle)
# Set pkgs after checks to avoid index out of range errors
pkgs = args[1:]
# Do operations
operations[args[0]](pkgs, handle)