import pyalpm
from libtwirl.errors import PackageNotFoundError
from libtwirl.core.database import search_repos
from libtwirl.core.database import fetch_local
from libtwirl.core.database import fetch_handle

def pkg_install(name):
	# Fetch important objects
	localdb = fetch_local()
	handle = fetch_handle()
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
	
	# Install the package
	t = handle.init_transaction()
	t.add_pkg(package)
	try:
		# Start transaction
		print(f"Attempting to install {package.db.name}/{name}-{package.version}")
		t.prepare()
		t.commit()
	except:
		# Handle error if package fails to install and unlock dbs
		t.release()
		raise Exception("Package failed to install.")
	# Unlock dbs after transaction
	t.release()
	print(f"Installed {name}-{package.version}")
	# Update the local database
	fetch_local()

