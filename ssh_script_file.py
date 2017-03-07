import sys
from threading import Thread

from pexpect import pxssh


hosts = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

hosts_list = [host for host in hosts.split(" ")]


def worker_ssh():
    ssh_instance = pxssh.pxssh()
    ssh_instance.login(host, username=username, password=password)
    ssh_instance.sendline(command)
    ssh_instance.prompt()
    print (ssh_instance.before.decode('utf-8'))
    ssh_instance.logout()


try:
    threads_host = []
    for host in hosts_list:
        t = Thread(target=worker_ssh)
        threads_host.append(t.start())


except pxssh.ExceptionPxssh as e:
    print ("pxssh failed on login")
    print (str(e))