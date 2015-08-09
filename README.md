# Overview

Simple Minecraft Server Wrapper (SMSW) keeps your server up to date with the current snapshot version of Minecraft from Mojang.  Its less than 100 lines of code and designed to be super simple & lightweight.

I've tested this under Mac OSX.  It should work fine on most *nix distributions.  Not tested on windows.

If there's interest from folks I'll consider updating it with more features.

# Installation

1. Download app.py to your minecraft server folder.
2. Make sure you have a correct eula.txt file accepting the license agreement.
3. run from terminal using 'python app.py'

# Features

- Checks for the latest Minecraft snaphsot version from Mojang's servers
- Contintually checks for an updated snapshot server even while the Minecraft server is running.
- Gracefully stops the server when a new version is detected.
- Downloads the latest snapshop and restarts the server.
- 