# Overview

Simple Minecraft Server Wrapper (SMSW) keeps your server running and up to date with the latest snapshot or production version of Minecraft from Mojang.

This has been tested successfully on Mac, Debian, and Windows 7.

If there’s interest from folks I’ll consider updating it with more features.

# Installation

1. Download app.py to your minecraft server folder.
2. If running the server for the first time, have a correct eula.txt file (accept the license agreement).
3. From terminal run by typing ‘python app.py’

# Usage
app.py [-h] [-m MEMMIN] [-x MEMMAX] [-p PATH] [-g] [-d]

-h, --help  Show this help message and exit<br />
-m MEMMIN   Sets the minimum/initial memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)<br />
-x MEMMAX   Sets the maximum memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)<br />
-p PATH     Set the local path where you want the server downloaded and ran, default is local directory<br />
-g          Utilize the Minecraft server GUI, default is off<br />
-d          Use development snapshots instead of stable Minecraft releases<br />


# Features

- Automatically checks for and downloads the latest snapshot or production version of Minecraft.
- Starts Minecraft and continually checks for new snapshot or production versions in the background.
- Fault tolerant! If your server crashes the wrapper will reqtart it.
- Allows command line arguments for memory settings, GUI mode, path, and snapshot/production version.
- Stops the server when a new version is detected and downloads it.
- Messages in game to let users know that the server is rebooting for maintenance.
- Restarts the server and keeps monitoring for new releases.
- Written in Python!
