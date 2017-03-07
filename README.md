# SSHScript
It is a simple script where you can specify your hosts, username and pass and sending commands to different hosts.

First argument, hosts (separated by space), I am working for reading the hosts from a txt, and you can specify some specific format for usename and password
Second argument username
Third argument password
Fourth argument command to execute


All this ssh conections are executed in different threads then you don't bother the rest of conection. I am working for the migration from python2.7 using the threading package to python 3.5 using Asyncio. This will be useful if you want to connect to a lot of machines 


example:
  ssh_script_file.py "host1 host2" username password "command"
