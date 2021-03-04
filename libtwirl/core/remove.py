import pyalpm
from libtwirl.errors import PackageNotFoundError
from libtwirl.core.database import search_repos
from libtwirl.core.database import fetch_local
from libtwirl.core.database import fetch_handle

def pkg_remove(pkgs, options = None): # Function to uninstall packages
	# Fetch important objects
	localdb = fetch_local()
	handle = fetch_handle()
	targets = []
	for name in pkgs:
		# Find the package in the localdb
		package = localdb.get_pkg(name)
		# Check if the package is installed
		if not package:
			raise PackageNotFoundError(name)
		# Add the package to the list of packages to install
		targets.append(package)
	# Print a list of packages to install
	formatted_targets = []
	[formatted_targets.append(f"{pkg.db.name}/{pkg.name}-{pkg.version}") for pkg in targets]
	print('\n'.join(formatted_targets))
	# Remove the packages
	t = handle.init_transaction()
	[t.remove_pkg(pkg) for pkg in targets]
	try:
		# Start transaction
		print("Starting removal.")
		t.prepare()
		t.commit()
	except:
		# Handle error if package fails to install and unlock dbs
		t.release()
		raise Exception("Package(s) failed to uninstall.")
	# Unlock dbs after transaction
	t.release()
	print(f"Removed all targets.")
	# Update the local database
	fetch_local()

