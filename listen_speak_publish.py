# Listen / Speaker  PC

## Modules

import subprocess
import time

## Variables

lap_send = 0.79
lap = 1
unit = ""

name_receive_file = "receive_file"
name_command_file = "command_file"


HOST = "192.168.0.189"
PORT = "9200"

## Code

    ## Prise de controle

subprocess.run("echo '+++ATC' | nc -N %s %s" % (HOST,PORT),shell=True)

    ## Sending and listening

while True:
    command = open("%s.txt"%(name_command_file),"r+")
    commandlines = command.read()
    if commandlines != "":
        for x in commandlines.split("\n"):
            xlen = str(len(x))
            if x != "":
                subprocess.run("echo 'AT*SENDIM,%s,1,noack,%s' | nc -N %s %s" % (xlen,x,HOST,PORT),shell=True)
                time.sleep(lap_send)
        open("%s.txt"%(name_command_file),"w+")
    command.close()
    subprocess.run("nc -w %s%s %s %s >> %s.txt" % (str(lap),unit,HOST,PORT,name_receive_file),shell=True)