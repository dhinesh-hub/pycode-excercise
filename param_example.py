#ssh into a client and read lines from the client
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.3.128.37',username='root',password='cohorocks1')
stdin,stdout,stderr = ssh.exec_command("sudo uptime")
stdin.write('cohorocks1')  # since sudo is used in previoud line input passowrd for root
print stdout.readlines()
stdin,stdout,stderr = ssh.exec_command("cat /etc/network/interfaces")
data = stdout.read().splitlines() #this will split the lines
print data
for line in data:
    print line 


