# Overview

Simple Minecraft Server Wrapper (SMSW) keeps your server up to date with the latest snapshot or production version of Minecraft from Mojang.  Its less than 100 lines of code and designed to be super lightweight and simple.

This has been tested successfully on Mac and Windows 7.

If there’s interest from folks I’ll consider updating it with more features.

# Installation

1. Download app.py to your minecraft server folder.
2. If running the server for the first time, have a correct eula.txt file (accept the license agreement).
3. From terminal run by typing ‘python app.py’

# Usage
app.py [-h] [-m MEMMIN] [-x MEMMAX] [-p PATH] [-g] [-d]

-h, --help  Show this help message and exit\n
-m MEMMIN   Sets the minimum/initial memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)\n
-x MEMMAX   Sets the maximum memory usage for the Minecraft server in GB (ex: 1, 2, 3, 4)\n
-p PATH     Set the local path where you want the server downloaded and ran, default is local directory\n
-g          Utilize the Minecraft server GUI, default is off\n
-d          Use development snapshots instead of stable Minecraft releases\n


# Features

- Automatically checks for and downloads the latest snapshot or production version of Minecraft.
- Starts Minecraft and continually checks for new snapshot or production versions in the background.
- Allows command line arguments for memory settings, GUI mode, path, and snapshot/production version
- Stops the server when a new version is detected and downloads it.
- Restarts the server and keeps monitoring for new releases.
- Written in Python!
