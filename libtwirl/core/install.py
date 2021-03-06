import pyalpm
import libtwirl.core.transaction as transaction
from libtwirl.errors import PackageNotFoundError
from libtwirl.core.database import search_repos
from libtwirl import handle


def pkg_install(pkgs, options = None):
	"""
	Function to install packages
	"""

	# Fetch important objects
	localdb = handle.get_localdb()
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
	print(f"\n\033[1mPackages to install ({len(targets)}):\033[0m")
	formatted_targets = []
	[formatted_targets.append(f"{pkg.db.name}/{pkg.name}-{pkg.version}") for pkg in targets]
	print('\n'.join(formatted_targets), "\n")
	# Install the packages
	t = transaction.transaction_init()
	[t.add_pkg(pkg) for pkg in targets]
	transaction.transaction_commit(t)
