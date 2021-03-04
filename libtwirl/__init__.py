import pyalpm
from pyalpm import Handle
from libtwirl.core.database import register_repos
# TODO (POSSIBLY): wrap all in a single function for a frontend to use instead (and allow for changing root dir)
handle = Handle("/", "/var/lib/pacman")
  
# Register synced repositories automatically for now
# Preferred if a frontend does it themselves, see TODO below
# TODO: parse config to find repositories to register (or make the frontend handle it) instead of arbitrary repo list at end
# TODO: parse config and mirrorlist to find mirrors instead of arbitrary mirror
register_repos({
    "core": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"],
    "extra": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"],
    "community": ["https://mirror.osbeck.com/archlinux/$repo/os/$arch"]
    })
