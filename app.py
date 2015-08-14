# Simple Minecraft Server Wrapper for snapshots.
# ======
# Finds the latest snapshot version, downloads and runs it.  Then
# every hour it checks for a new snapshot release.  If it finds one,
# it stops the server, downloads the update and restarts with the
# newest version.

# Test commit dyonak

import time
import subprocess
import json
import urllib2
import urllib
import sys
import getopt

# Global Settings

minecraft_version_url = 'https://s3.amazonaws.com/Minecraft.Download/versions/versions.json'
check_for_new_versions_frequency = 3600 # every hour
mc_server = 'minecraft_server.jar' # server file name
memmin = 1
memmax = 1
args2 = 'nogui'
current_ver = ''
run = 0


def process_args():
    myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
    ###############################
    # o == option
    # a == argument passed to the o
    ###############################
    for o, a in myopts:
        if o == '-memmin':
            memmin=a
        elif o == '-memmax':
            memmax=a


# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"]
	print '--- The latest verison of Minecraft Snapshopt is', ver
	return ver

# TODO - Implement function to determine currently installed version
# BUG - Program will download new version at start every time
# Check installed version
def get_installed_version():
	return 1


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
		print '--- Starting Server.'
		run = 1
		command = 'java -jar ' + '-Xms' + memmin + 'G' + '-Xmx' + memmax + 'G' + ' ' + mc_server + ' ' + args2
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
