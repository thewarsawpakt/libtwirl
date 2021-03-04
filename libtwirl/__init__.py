import pyalpm
from pyalpm import Handle
# TODO (POSSIBLY): wrap all in a single function for a frontend to use instead (and allow for changing root dir)
handle = Handle("/", "/var/lib/pacman")

# Fetch the local database
# Preferred if other functions do it instead themselves of relying on this variable for updatedness
localdb = handle.get_localdb()

def register_repos(repolist, siglvl = pyalpm.SIG_DATABASE_OPTIONAL): # Function to register synced repositories
	for reponame in repolist:
		# Register repositories into the handle
		# TODO (POSSIBLY): Add a way to specify the signature level of repositories (independently)
		handle.register_syncdb(reponame, siglvl)

def search_repos(pkgname, find_provides = True): # Function to search the synced repositories
	syncdbs = handle.get_syncdbs()
	packages = []
	# Iterate through list of synced databases for exact packages
	for repo in syncdbs:
		pkg = repo.get_pkg(pkgname)
		if not pkg is None:
			# Append package to list
			packages.append(pkg)
	# If find_provides is false, skip this step
	if find_provides:
		# Iterate through list again to find provides
		# Iterating twice is to make sure the exact package, if it exists, always shows up first
		for repo in syncdbs:
			pkgs = repo.search(pkgname)
			# Iterate though broader list to find package providers
			for pkg in pkgs:
				if pkgname in pkg.provides:
					# Append package provider to list
					packages.append(pkg)
	if len(packages) > 0:
		# Return the list of found packages
		return packages
	else:
		# Return None if there were no packages found
		return None # Would it be preferred if this only returned an empty list instead of None?
  
# Register synced repositories automatically for now
# Preferred if a frontend does it themselves, see TODO below
# TODO: parse config to find repositories to register (or make the frontend handle it) instead of arbitrary repo list at end
register_repos(["core", "extra", "community"])
