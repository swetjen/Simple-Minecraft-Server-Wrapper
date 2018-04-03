# Simple Minecraft Server Wrapper for snapshots and production releases.
# ======
# Finds the latest snapshot or production version, downloads and runs it.  Then
# every hour it checks for a new snapshot or production release.  If it finds one,
# it stops the server, downloads the update and restarts with the newest version.

import time, json, urllib2, urllib, argparse, os, random
from ServerManager import ServerManager

# Global Settings

minecraft_version_url = 'https://s3.amazonaws.com/Minecraft.Download/versions/versions.json'
check_for_new_versions_frequency = 3600  # every hour
mc_server = 'minecraft_server.jar'  # server file name
current_ver = ''

#test
# Process command line arguments for memory settings
def process_args():
    global results
    parser = argparse.ArgumentParser(description="Simple Minecraft Server Wrapper")
    parser.add_argument("-m", action='store', dest='memmin',
                        help="Sets the minimum/initial memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)",
                        type=int, default=1)
    parser.add_argument("-x", action='store', dest='memmax',
                        help="Sets the maximum memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)", type=int,
                        default=1)
    parser.add_argument("-p", action='store', dest='path',
                        help="Set the local path where you want the server downloaded and ran, default is local directory",
                        type=str, default='')
    parser.add_argument("-g", action='store_true', dest='gui', help="Utilize the Minecraft server GUI, default is off")
    parser.add_argument("-d", action='store_true', dest='dev',
                        help="Use development snapshots instead of stable Minecraft releases")
    parser.add_argument("-r", action='store_true', dest='raffle', help="Occasionally rewards server players.")
    parser.add_argument("-m", action='store', dest='memmin', help="Set the minimum memory for Minecraft in GB (ex: 1, 2, 3, 4).  Default is 1.", type=int, default=1)
    parser.add_argument("-x", action='store', dest='memmax', help="Set the maximum memory for Minecraft in GB (ex: 1, 2, 3, 4).  Default is 1.", type=int, default=1)
    parser.add_argument("-p", action='store', dest='path', help="Specify another directory to run the server.", type=str, default='')
    parser.add_argument("-g", action='store_true', dest='gui', help="   Utilize the Minecraft server GUI.  Default is off")
    parser.add_argument("-s", action='store_true', dest='stable', help="Use stable release of Minecraft instead of development snapshots.")
    results = parser.parse_args()
    if results.path != '': results.path = os.path.join(results.path, '')  # Path handling to include the trailing slash
    return



# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
	source = urllib2.urlopen(minecraft_version_url)
	data = json.load(source)
	ver = data["latest"]["snapshot"] if results.stable == False else data["latest"]["release"]
	logpr('--- The latest version of Minecraft is', ver)
	return ver

# Download the latest version JSON file for Minecraft and see what the latest version is
def get_version():
    source = urllib2.urlopen(minecraft_version_url)
    data = json.load(source)
    ver = data["latest"]["snapshot"] if results.stable == False else data["latest"]["release"]
    print '--- The latest version of Minecraft is', ver
    return ver


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
    jarfile.retrieve(
        "https://s3.amazonaws.com/Minecraft.Download/versions/" + version + "/minecraft_server." + version + ".jar",
        results.path + mc_server)
    print "--- Download complete."


# Supervisor program
def main():
    process_args()
    server = ServerManager(results.path, mc_server, results.memmin, results.memmax, results.gui)
    global current_ver
    print '*' * 40
    print '* Simple Minecraft Server Wrapper'
    print '*' * 40
    latest_ver = str(get_version())
    if current_ver != latest_ver:
        download_server(latest_ver)
        current_ver = latest_ver
    if not server.online:
        server.start()
        time.sleep(5)
        while server.online:
            print '--- Checking for new versions in ' + str(check_for_new_versions_frequency) + ' seconds.'
            time.sleep(check_for_new_versions_frequency)
            if server.crash_check():
                del server
                main()
            print '--- Checking for a new version...'
            server.message('Checking for a new version...')
            # Checking for new version
            if not up_to_date(current_ver):
                # new version detected
                time.sleep(30)
                server.shutdown()
                del server
                time.sleep(5)
                print '--- Server stopped'
                main()
            else:
                server.message('No new version detected.')
                if results.raffle:
                    time.sleep(3)
                    server.message('Calculating merit based rewards...')
                    raffle_chance = random.randint(1, 10)
                    if raffle_chance in (1, 2, 3, 4, 5):
                        time.sleep(3)
                        server.message('Sorry, maybe next time.')
                    elif raffle_chance == 6:
                        server.message('give @a minecraft:diamond 10', True)
                    elif raffle_chance == 7:
                        server.message('give @a minecraft:coal_block 10', True)
                    elif raffle_chance == 8:
                        server.message('give @a minecraft:cake 1', True)
                    elif raffle_chance == 9:
                        server.message('give @a minecraft:cooked_beef 64', True)
                    elif raffle_chance == 10:
                        server.message('give @a minecraft:rabbit_foot 1', True)


# Start when run.
if __name__ == '__main__':
    main()
