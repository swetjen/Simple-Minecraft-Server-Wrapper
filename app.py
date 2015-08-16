# Simple Minecraft Server Wrapper for snapshots and production releases.
# ======
# Finds the latest snapshot or production version, downloads and runs it.  Then
# every hour it checks for a new snapshot or production release.  If it finds one,
# it stops the server, downloads the update and restarts with the newest version.

import time, subprocess, json, urllib2, urllib, argparse, os, hashlib, pprint

# Global Settings

minecraft_version_url = 'https://s3.amazonaws.com/Minecraft.Download/versions/versions.json'
check_for_new_versions_frequency = 60 # every hour
mc_server = 'minecraft_server.jar' # server file name
current_ver = ''
run = 0

# Process command line arguments for memory settings
def process_args():
	global results
	parser = argparse.ArgumentParser(description="Simple Minecraft Server Wrapper")
	parser.add_argument("-m", action='store', dest='memmin', help="Sets the minimum/initial memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)", type=int, default=1)
	parser.add_argument("-x", action='store', dest='memmax', help="Sets the maximum memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)", type=int, default=1)
	parser.add_argument("-p", action='store', dest='path', help="Set the local path where you want the server downloaded and ran, default is local directory", type=str, default='')
	parser.add_argument("-g", action='store_true', dest='gui', help="Utilize the Minecraft server GUI, default is off")
	parser.add_argument("-d", action='store_true', dest='dev', help="Use development snapshots instead of stable Minecraft releases")
	results = parser.parse_args()
	if results.path != '': results.path = os.path.join(results.path, '') # Path handling to include the trailing slash
   	return


# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"] if results.dev == True else data["latest"]["release"]
	print '--- The latest version of Minecraft is', ver
	return ver

def installed_version():
        #current_version = hashlib.md5(results.path + mc_server)
        #print current_version
        return current_version

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
	jarfile.retrieve("https://s3.amazonaws.com/Minecraft.Download/versions/"+ version + "/minecraft_server." + version + ".jar", results.path + mc_server)
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
		command = 'java -jar -Xms' + str(results.memmin) + 'G -Xmx' + str(results.memmax) + 'G ' + results.path + mc_server
		if results.gui == False: command += ' nogui'
		print '--- Starting server with command: ' + command;
		if results.path == '':mc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
		if results.path != '':mc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, cwd=results.path)
		time.sleep(5)
		while run == 1:
			print '--- Checking for new versions in ' + str(check_for_new_versions_frequency) + ' seconds.'
			print '--- Checking for a new version...'
			mc.stdin.write('say SMSW - Checking for new version...\n')
			mc.stdin.flush()
			if up_to_date(current_ver) == False:
				mc.stdin.write('say SMSW - New version detected, rebooting for update in 30 seconds...\n')
                                mc.stdin.flush()
				mc.stdin.write('say SMSW - Sorry for the troubles, have a diamond.\n')
                                mc.stdin.flush()
				mc.stdin.write('give @a minecraft:diamond 5\n')
                                mc.stdin.flush()
				time.sleep(30)
				mc.terminate()
				run = 0
				time.sleep(5)
				print '--- Server stopped'
				main()

# Start when run.
if __name__ == '__main__':
	main()
