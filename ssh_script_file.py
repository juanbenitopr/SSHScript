import argparse
import sys
from threading import Thread

from pexpect import pxssh


# hosts = sys.argv[1]
# username = sys.argv[2]
# password = sys.argv[3]
# command = sys.argv[4]


class SSHConnectionHosts():
    def __init__(self):
        self.hosts = []
        self.command = ""
        self.password = ""
        self.username = ""


    def add_hosts(self,hosts):
        if hosts: self.hosts = [ host for host in hosts.split(" ") ]

    def add_hosts_text(self,path):
        if path:
            hosts_in_file = open(path,'r')
            for host in hosts_in_file:
                self.hosts.append(host.replace("\n",""))


    def set_command (self,command):
        self.command = command

    def set_password(self,password):
        self.password  =password

    def set_username(self,username):
        self.username = username


    def worker_ssh(self,host):
        ssh_instance = pxssh.pxssh()
        ssh_instance.login(host, username=self.username, password=self.password)
        ssh_instance.sendline(self.command)
        ssh_instance.prompt()
        print (ssh_instance.before.decode('utf-8'))
        ssh_instance.logout()

    def run_ssh(self):
        try:
            threads_host = []
            for host in self.hosts:
                t = Thread(target=self.worker_ssh, kwargs={'host':host})
                threads_host.append(t.start())
        except pxssh.ExceptionPxssh as e:
            print ("pxssh failed on login")
            print (str(e))

sshconnection = SSHConnectionHosts()
parser = argparse.ArgumentParser(prog='ssh_script_file',description='Sending commands to many hosts')

parser.add_argument('-hosts', help="Specify name of the hosts by command line")
parser.add_argument('-H', help = "Specify file where you store your host names")
parser.add_argument('-u', help ="Specify your username for hosts")
parser.add_argument('-p', help="Specify the password for the entry to the hosts")
parser.add_argument('-c', help="The command to use in the different servers")


args = parser.parse_args()
sshconnection.add_hosts(args.hosts)
sshconnection.add_hosts_text(args.H)
sshconnection.set_username(args.u)
sshconnection.set_password(args.p)
sshconnection.set_command(args.c)
sshconnection.run_ssh()