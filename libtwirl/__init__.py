import pyalpm
from pyalpm import Handle
# TODO (POSSIBLY): wrap all in a single function for a frontend to use instead (and allow for changing root dir)
handle = Handle("/", "/var/lib/pacman")

# Now some of the keen eyed amongst you may have noticed
# that this is an import statement right smack-dab in the
# middle of code. Why? Because circular imports. database.py
# (the file that's being imported) imports the handle variable
# from itself, but if this import statement were at the top,
# handle wouldn't be defined yet and we would have ciruclar
# imports. - Sophon96
from libtwirl.core.database import register_repos
  
# Register synced repositories automatically for now
# Preferred if a frontend does it themselves, see TODO below
# TODO: parse config to find repositories to register (or make the frontend handle it) instead of arbitrary repo list at end
# TODO: parse config and mirrorlist to find mirrors instead of arbitrary mirror
register_repos({
    "core": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"],
    "extra": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"],
    "community": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"]
    })
