#!/usr/bin/env python
import paramiko
session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect("stones.cse.buffalo.edu", username = "****", password = "****")
#attempt to make dir
stdout, stderr = session.exec_command("ps aux");
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
outlines2=stderr.readlines()
resp2=''.join(outlines2)
print(resp2)
session.close()
