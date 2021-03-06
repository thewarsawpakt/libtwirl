import libtwirl.core.database as database
import pyalpm
def get_option_value(options, option_name, default = False):
	"""
	Get the options from the dictionary
	"""

	# This is so we can set the default values easily
	if not options: # Return default if the options are None
		return default
	elif not option_name in options.keys(): # Return default if there is no key
		return default
	else:
		return options[option_name]

def transaction_init(handle, options = None):
	"""
	Start the transaction using the options
	"""

	# Initialise the transation and set the values
	t = handle.init_transaction(
		cascade=get_option_value(options, "cascade"),
		nodeps=get_option_value(options, "nodeps"),
		force=get_option_value(options, 'force'),
		dbonly=get_option_value(options, 'dbonly'),
		downloadonly=get_option_value(options, 'downloadonly'),
		nosave=get_option_value(options, 'nosave'),
		recurse=(get_option_value(options, 'recursive')),
		#recurseall=(get_option_value(options, 'recursive', 0) > 1),
		unneeded=get_option_value(options, 'unneeded'),
		alldeps=(get_option_value(options, 'mode', None) == pyalpm.PKG_REASON_DEPEND),
		allexplicit=(get_option_value(options, 'mode', None) == pyalpm.PKG_REASON_EXPLICIT))
	return t

def transaction_commit(t):
	"""
	Do the transaction itself
	"""

	try:
		# Start transaction
		print("Starting transaction.")
		t.prepare()
		t.commit()
	except:
		# Handle error if package fails to install and unlock dbs
		t.release()
		raise Exception("Transaction failed.")
	# Unlock dbs after transaction
	t.release()
	print(f"Transaction complete.")
