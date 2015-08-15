# Simple Minecraft Server Wrapper for snapshots and production releases.
# ======
# Finds the latest snapshot or production version, downloads and runs it.  Then
# every hour it checks for a new snapshot or production release.  If it finds one,
# it stops the server, downloads the update and restarts with the newest version.

import time
import subprocess
import json
import urllib2
import urllib
import argparse

# Global Settings

minecraft_version_url = 'https://s3.amazonaws.com/Minecraft.Download/versions/versions.json'
check_for_new_versions_frequency = 3600 # every hour
mc_server = 'minecraft_server.jar' # server file name
current_ver = ''
run = 0

# Process command line arguments for memory settings
def process_args():
	global results
	parser = argparse.ArgumentParser(description="Simple Minecraft Server Wrapper")
	parser.add_argument("-m", action='store', dest='memmin', help="Sets the minimum/initial memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)", type=int, default=1)
	parser.add_argument("-x", action='store', dest='memmax', help="Sets the minimum/initial memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)", type=int, default=1)
	parser.add_argument("-g", action='store_true', dest='gui', help="Utilize the Minecraft server GUI, default is off")
	parser.add_argument("-d", action='store_true', dest='dev', help="Use development snapshots instead of stable Minecraft releases")
	results = parser.parse_args()
   	return


# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"] if results.dev == True else data["latest"]["release"]
	print '--- The latest version of Minecraft is', ver
	return ver

# TODO - Implement function to determine currently installed version
# BUG - Program will download new version at start every time

# Checks if the latest version matches current version.
def up_to_date(current_ver):
	temp_ver = str(get_version())
	if current_ver != temp_ver:
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


# Supervisor program
def main():
	process_args()
	global current_ver
	global run
	print '*' * 40
	print '* Simple Minecraft Server Wrapper'
	print '*' * 40
	latest_ver = str(get_version())
	if current_ver != latest_ver:
		download_server(latest_ver)
		current_ver = latest_ver
	if run == 0:
		run = 1
		command = 'java -jar -Xms' + str(results.memmin) + 'G -Xmx' + str(results.memmax) + 'G ' + mc_server
		if results.gui == False:
			command += ' nogui'
		print '--- Starting server with command: ' + command;
		mc = subprocess.Popen(command, shell=True)
		time.sleep(5)
		while run == 1:
			print '--- Checking for new versions in ' + str(check_for_new_versions_frequency) + ' seconds.'
			time.sleep(check_for_new_versions_frequency)
			print '--- Checking for a new version...'
			if up_to_date(current_ver) == False:
				mc.terminate()
				run = 0
				time.sleep(5)
				print '--- Server stopped'
				main()

# Start when run.
if __name__ == '__main__':
	main()
