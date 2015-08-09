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
current_ver = ''
run = 0


# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"]
	print '--- The latest verison of Minecraft Snapshopt is', ver
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
		print '--- Starting Server.'
		run = 1
		mc = subprocess.Popen(['java -jar ' + mc_server], shell=True)
		time.sleep(5)
		while run == 1:
			print '--- Checking for new versions in ' + str(check_for_new_versions_frequency) + ' seconds.'
			time.sleep(check_for_new_versions_frequency)
			print '--- Checking for a new version...'
			if up_to_date(current_ver, latest_ver) == False:
				mc.terminate()
				run = 0
				time.sleep(5)
				print '--- Server stopped'
				main()

# Start when run.
if __name__ == '__main__':
	main()


 

