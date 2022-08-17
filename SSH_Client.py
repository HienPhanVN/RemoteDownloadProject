# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import paramiko
from paramiko.client import SSHClient, AutoAddPolicy, RejectPolicy

class SSH_Client:
    def connect_ssh():
        hostname = 'thehieshop.duckdns.org'
        port = 22
        username = 'root'
        password = 'infotv.vn'

        if __name__ == "__main__":
            paramiko.util.log_to_file('paramiko.log')
            s = paramiko.SSHClient()
            s.set_missing_host_key_policy(AutoAddPolicy)
            s.connect(hostname, port, username, password)
            stdin, stdout, stderr = s.exec_command('ifconfig')
            print(stdout.read())
            stdout.read()
            s.close()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
