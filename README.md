# Overview

Simple Minecraft Server Wrapper (SMSW) keeps your server up to date with the latest snapshot version of Minecraft from Mojang.  Its less than 100 lines of code and designed to be super lightweight and simple.

This has been tested successfully on Mac and Windows 7.

If there’s interest from folks I’ll consider updating it with more features.

# Installation

1. Download app.py to your minecraft server folder.
2. If running the server for the first time, have a correct eula.txt file (accept the license agreement).
3. From terminal run by typing ‘python app.py’

# Features

- Automatically checks for and downloads the latest snapshot version of Minecraft.
- Starts Minecraft and continually checks for new Snapshots versions in the background.
- Allows command line arguments for Minecraft server memory settings
- Stops the server when a new version is detected and downloads it.
- Restarts the server and keeps monitoring for new releases.
- Written in Python!
- Add command line arguments for Minecraft server memory settings