import pyalpm
from pyalpm import Handle
handle = Handle("/", "/var/lib/pacman")

# Local DB
localdb = handle.get_localdb()

# Synced DBs
handle.register_syncdb("core", pyalpm.SIG_DATABASE_OPTIONAL)

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
		# This is to make sure the exact package, if it exists, always shows up first
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
		return None
  
