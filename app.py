# Simple Minecraft Server Wrapper for snapshots

import time
import subprocess
import json
import urllib2
import urllib

# Global Settings

minecraft_version_url = 'https://s3.amazonaws.com/Minecraft.Download/versions/versions.json'
check_for_new_versions_frequency = 15 # every hour
mc_server = 'minecraft_server.jar' # server file name
current_ver = ''
run = 0


# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"]
	print '--- The current verison of Minecraft Snapshopt is', ver
	return ver

# Checks if the latest version matches current version.
def up_to_date(current_ver, latest_ver):
	if current_ver != latest_ver:
		print '--- New version detected.'
		return False
	else:
		print '--- Up to date.'
		return True

# Downloads and saves the latest minecraft server.
def download_server(version):
	jarfile = urllib.URLopener()
	print "--- Downloading", version
	jarfile.retrieve("https://s3.amazonaws.com/Minecraft.Download/versions/"+ version + "/minecraft_server." + version + ".jar", mc_server)
	print "--- Download complete."

# Start the server
def start_server():
	global run
	run = 1
	mc = subprocess.Popen(['java -jar ' + mc_server], shell=True)
	return

# Stop the server
def stop_server():
	global run
	print '--- Stopping Server.'
	# mc.terminate()
	time.sleep(5)
	print '--- Server stopped'
	run = 0
	return

# Supervisor program

def main():
	global current_ver
	global run
	print '*' * 40
	latest_ver = str(get_version())
	if current_ver != latest_ver:
		download_server(latest_ver)
		current_ver = latest_ver
	if run == 0:
		print '--- Starting Run'
		# simulate new version
		# start server
		run = 1 # kill this after test
		while run == 1:
			print '--- Checking for new versions in ' + str(check_for_new_versions_frequency) + ' seconds.'
			time.sleep(check_for_new_versions_frequency)
			print '--- Checking for a new version...'
			if up_to_date(current_ver, latest_ver) == False:
				stop_server()
				main()


if __name__ == '__main__':
	main()






### startup
### Get Versions Json 
### Find the latest version of Minecraft 
### Download the latest version
### Run Minecraft

'''
is this startup?
	Get the latest version
	Check it against current version
	if current and latesst == equal
		keep running	
	else 
		stop_server
		download_server
		start server
'''

# Store operating version as a variable and itermittantly check to see if there's a new server
# If so, Stop the server with a friendly message and re-run 


# Download Latest Version of Minecraft and Save to working folder


# Run Minecraft and shutdown Minecraft


