# SSHScript
It is a simple script where you can specify your hosts, username and pass and sending commands to different hosts.

All ssh conections are executed in different threads then you don't bother the rest of connection. I am working for the migration from python2.7 using the threading package to python 3.5 using Asyncio. This will be useful if you want to connect to a lot of machines

The script has a few options from specify hosts in txt to do all the options from command line you just have to write the command -h for view the help

example:
  ssh_script_file.py -h
