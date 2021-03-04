import pyalpm
from libtwirl.errors import PackageNotFoundError
from libtwirl.core.database import search_repos
from libtwirl.core.database import fetch_local
from libtwirl.core.database import fetch_handle

def pkg_install(pkgs, options = None): # Function to install packages
	# Fetch important objects
	localdb = fetch_local()
	handle = fetch_handle()
	targets = []
	for name in pkgs:
		# Check if the package is already installed before installing
		if localdb.get_pkg(name):
			print(f"WARNING: Package {name} is already installed.")
		# Find package in the provided sync repos
		package = search_repos(name)
		# Make sure the package exists before installing
		if package is None:
			raise PackageNotFoundError(name)
		else: # Set the package to the first index of the array since we know it exists
			package = package[0]
		# Add the package to the list to install
		targets.append(package)
	# Print a list of packages to install
	formatted_targets = []
	[formatted_targets.append(f"{pkg.db.name}/{pkg.name}-{pkg.version}") for pkg in targets]
	print('\n'.join(formatted_targets))
	# Install the packages
	t = handle.init_transaction()
	[t.add_pkg(pkg) for pkg in targets]
	try:
		# Start transaction
		print("Starting installation.")
		t.prepare()
		t.commit()
	except:
		# Handle error if package fails to install and unlock dbs
		t.release()
		raise Exception("Package(s) failed to install.")
	# Unlock dbs after transaction
	t.release()
	print("Installed all targets.")
	# Update the local database
	fetch_local()

