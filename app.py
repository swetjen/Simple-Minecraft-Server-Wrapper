# Simple Minecraft Server Wrapper for snapshots

import time
import subprocess
import json
import urllib2
import urllib

# Global Settings

minecraft_version_url = 'https://s3.amazonaws.com/Minecraft.Download/versions/versions.json'
check_for_new_versions_frequency = 3600 # every hour
mc_server = 'minecraft_server.jar' # server file name

#

# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"]
	print 'The current verison of Minecraft Snapshopt is', ver
	return ver

def startup(current_ver):
	latest_ver = get_version
	print latest_ver
	if len(current_ver) < 1:
		download_server(latest_ver)
		current_ver = latest_ver
		return

def download_server(version):
	jarfile = urllib.URLopener()
	print "Im downloading", version
	jarfile.retrieve("https://s3.amazonaws.com/Minecraft.Download/versions/"+ version + "/minecraft_server." + version + ".jar", mc_server)
	print "Download complete."


def start_server():
	if status == 1:
		raise 'Sever already running'
	else:
		status = 1
		mc = subprocess.Popen(['java -jar ' + mc_server], shell=True)
	return

def stop_server():
	status = 0
	mc.terminate()
	time.sleep(5)
	return

#
# MAIN PROGRAM
#

def main():
	startup(current_ver)


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


