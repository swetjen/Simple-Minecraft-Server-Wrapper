# Overview

Simple Minecraft Server Wrapper (SMSW) keeps your server up to date with the current snapshot version of Minecraft from Mojang.  Its less than 100 lines of code and designed to be super simple & lightweight.

I've tested this under Mac OSX.  It should work fine on most *nix distributions.  Not tested on windows.

If there's interest from folks I'll consider updating it with more features.

# Installation

1. Download app.py to your minecraft server folder.
2. If running the server for the firset time, have a correct eula.txt file (accept the license agreement).
3. From terminal run by typing 'python app.py'

# Features

- Checks for the latest Minecraft snaphsot version from Mojang's servers
- While the server is running, checks for an updated snapshot in the background.
- Gracefully stops the server when a new version is detected.
- Automatically downloads the latest snapshop and restarts the server with the new version.
