import pyalpm
from libtwirl import handle


def register_repos(repolist, architecture = "x86_64", siglvl = pyalpm.SIG_DATABASE_OPTIONAL):
	"""
	Function to register synced repositories
	"""

	for reponame in repolist.keys():
		# Register repositories into the handle
		# TODO (POSSIBLY): Add a way to specify the signature level of repositories (independently)
		repo = handle.register_syncdb(reponame, siglvl)
		# Make server list for database
		repo_servers = []
		for rawurl in repolist[reponame]:
		    # Substitute URL variables
		    url = rawurl.replace("$repo", reponame)
		    url = url.replace("$arch", architecture)
		    # Add URL to tmplist
		    repo_servers.append(url)
		# Add server list to the repository
		repo.servers = repo_servers


def search_repos(pkgname, find_provides = True):
	"""
	Function to search the synced repositories
	"""

	syncdbs = handle.get_syncdbs()
	packages = []	# List of packages that have the name or provide the requested package
	# Iterate through list of synced databases for exact packages
	# This gets a package from every repository, if it exists
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
		return None
