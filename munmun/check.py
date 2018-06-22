#!/usr/bin/python2
import commands
import time

option='''
press 1 to check internet cable on your machine.
press 2 to check internet access.
press 3 to check for google access.'''
print option
choice=raw_input("enter your choice:")

if choice== '1':
    print"plz wait internet  cable is being checked by current os"
    time.sleep(3)
    cable_check=commands.getoutput("mii-tool eno1")

    if 'link ok' in cable_check:
      print"cable is connected"
      out="connected"
      commands.getoutput('notify send'+out)
      commands.getoutput('echo connected |festival --tts')
    else:
      print"cable is not connected"
      out="not connected"
      commands.getoutput('notify send '+out)
      commands.getoutput('echo not connected | festival --tts')
elif choice== '2':
     print " internet connectivity is checking in a while.."
     time.sleep(2)
     y = commands.getoutput('ping -c 1 -w 1 8.8.8.8')
     print y
     
     if '0% packet loss ' in y :
            print "internet connectivity is all right"
            out="internet is alright"
            commands.getoutput('notify send ' +out)
            commands.getoutput('echo internet is all right |festival --tts')
     else:
            print"internet connectivity is not all right"
            out="no internet"
            commands.getoutput('notify send '+out)
            commands.getoutput('echo no internet | festival --tts')
elif choice=='3':
      print"loading google web page"
      time.sleep(2)
      z=commands.getoutput('firefox')
      commands.getoutput('notify send opening google page')
      commands.getoutput('echo loading google page | festival --tts')
else:
      print"wrong choice"
      print"TRY AGAIN !"
 
