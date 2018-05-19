
# Description			: This will list all the files in the given directory, it will also go through all the subdirectories as well

import os																		# Load the library module							

logdir  = os.getenv("logs")												# Set the variable logdir by getting the value from the OS environment variable logs
logfile = 'script_list.log'													# Set the variable logfile
path    = os.getenv("scripts")												# Set the varable path by getting the value from the OS environment variable scripts - 1.2

#path = (raw_input("Enter dir: "))										  # Ask the user for the directory to scan
logfilename = os.path.join(logdir, logfile)					  	# Set the variable logfilename by joining logdir and logfile together
log = open(logfilename, 'w')												    # Set the variable log and open the logfile for writing

for dirpath, dirname, filenames in os.walk(path):				# Go through the directories and the subdirectories
  for filename in filenames:											    	# Get all the filenames
    log.write(os.path.join(dirpath, filename)+'\n')					# Write the full path out to the logfile

print ("\nYour logfile " , logfilename, "has been created")		# Small message informing the user the file has been created
