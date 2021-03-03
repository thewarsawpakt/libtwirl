import pyalpm
from pyalpm import Handle

handle = Handle("/", "/var/lib/pacman")
localdb = handle.get_localdb()
coredb = handle.register_syncdb("core", pyalpm.SIG_DATABASE_OPTIONAL)
