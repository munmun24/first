#!/usr/bin/python2
import os
import time
import webbrowser
menu='''
Press 1 to check current time and date :
Press 2 to scan all your mac address in you current connected network:
Press 3 to shutdown your machine after 15 minutes:
Press 4 to search something on google:
Press 5 to logout your current machine:
Press 6 to shutdown all connected system in your current network:
Press 7 to update status in facebook:
Press 8 to list ip address of given website:
'''
print menu 
choice=raw_input()
if choice=="1":
	print"current date and time is:"
	print time.ctime()
elif choice=="2":
	os.system("nmap -v -sn 192.168.0.0/24")
elif choice=="3":
	os.system("shutdown -h +15")
elif choice=="4":
	find=raw_input("Enter your query:")
	webbrowser.open_new_tab("https://www.goggle.com/search? q="+find)
elif choice=="5":
	print "logging out from the system "
	os.system("gnome-session-quit")
elif choice=="6":
        print"close all your apps system is rebooting.."
        msg1="you can take some more time"
        time.sleep(2)
        msg2="please close all the apps as soon as possible"
        os.system("echo "+msg2+" | festival --tts")
        time.sleep(3)
        os.system("reboot")
else:
	print "invalid option"
