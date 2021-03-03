from twirl.errors import PackageNotFoundError
from twirl.core.debug import logging
from twirl import search_repos
from twirl import localdb

def search_for_pkg(name):
    potential_packages = localdb.search(name)
    i = None
    for i in potential_packages:
        if name in i.provides:
            break
    return i

def pkg(name, version=None, acc_deps=set()):

    if localdb.get_pkg(name):
        logging.info(f"WARNING: Package {name} is already installed.")
    package = search_repos(name)
    
    if not package:
        package = search_for_pkg(name)
        if package is None:
            raise PackageNotFoundError(name)
    else:
        package = package[0]
            
    logging.info(f"Attempting to install {name} (version {package.version})")
    #for file in package.files:
    #    print(file[0])

    print(f"{package.name}: {package.depends}")
    for dep in package.depends:
        if dep in acc_deps:
            continue
        else:
            acc_deps.add(dep)
        print(dep)
        if ".so" in dep:
            dep = dep.replace(".so", "")
        if ">=" in dep:
            pkg(dep.split(">=")[0], dep.split(">=")[1], acc_deps=acc_deps)
        elif "=" in dep:
            pkg(dep.split("=")[0], dep.split("=")[1])
        elif ".so" in dep:
            continue
        else: pkg(dep)
