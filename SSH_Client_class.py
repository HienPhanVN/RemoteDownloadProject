# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paramiko
from paramiko.client import SSHClient, AutoAddPolicy, RejectPolicy

class SSH_Client_class:
    def __init__(self):
        """Constructor"""
    def connect_ssh(self):
        hostname = 'thehieshop.duckdns.org'
        port = 22
        username = 'root'
        password = 'infotv.vn'
        paramiko.util.log_to_file('paramiko.log')
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(AutoAddPolicy)
        s.connect(hostname, port, username, password)
        command_for_ssh_server = "mount -t cifs -o username=admin,password=admin1 '//192.168.1.9/GoFlex Home Public' ~/NAS -o vers=1.0 & cd \"/root/NAS/Apps/Arm Script/RemoteDownloadProject\" & python3 server_side.py -url https://file-examples.com/storage/fe5947fd2362fc197a3c2df/2017/04/file_example_MP4_480_1_5MG.mp4 -code 5995"
        stdin, stdout, stderr = s.exec_command(command_for_ssh_server)
        print(stdout.read())
        stdout.read()
        s.close()

