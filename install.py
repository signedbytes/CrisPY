#!/usr/bin/env python

import os
import webbrowser,os,sys,re
import commands
import time



class indi:
	
	def __init__(self,):

		choice = raw_input("\033[1;36m your Option(y/n/r/h/p) : \033[1;m")

		if choice == "y":
			self.maxx = commands.getstatusoutput("echo $USER")
			self.curr = commands.getstatusoutput("ls /home/")
			self.new = tuple(x for x in self.curr if x <> 0)
			for i in self.new:
				self.black = os.chdir("/home/")
				self.pwd = os.getcwd()
				
			        self.do = os.popen("wget http://localhost/crispy_ver_1.0.zip")
				time.sleep(1)
				
                                self.unzip = commands.getoutput("unzip crispy_ver_1.0.zip")
				
				commands.getstatusoutput("chmod -R 0777 crispy/")
			self.maxx = commands.getstatusoutput("echo $USER")
			self.curr = commands.getstatusoutput("ls /home/crispy/")
			self.new = tuple(x for x in self.curr if x <> 0)
			for i in self.new:
				self.black = os.chdir("/home/crispy/")
				self.pwd = os.getcwd()	
           

				print "have pacience ...... exploiter is starting ....... "
				os.system('python main.py')
       		
			

		elif choice == "n":
			print ""
			print "Good Buy Have A Nice day :) "
                if choice == "r":

                	webbrowser.open('http://pastebin.com/raw.php?i=Nx2yimKC')
                if choice == "p":


			self.maxx = commands.getstatusoutput("echo $USER")
			self.curr = commands.getstatusoutput("ls /home/crispy")
			self.new = tuple(x for x in self.curr if x <> 0)
			for i in self.new:
				self.black = os.chdir("/home/crispy")
				self.pwd = os.getcwd()
				os.system('python main.py') 	


                if choice == "h":

                	os.system('clear')
                	print "yes for installtion " # write what u want 
                	print "no for EXIT "
                	print ""

                else:
                	print "s"
		           



	boring = """\033[1;32m
                                       
               
 
   _____      _     _______     __
  / ____|    (_)   |  __ \ \   / /
 | |     _ __ _ ___| |__) \ \_/ /
 | |    | '__| / __|  ___/ \   /  
 | |____| |  | \__ \ |      | |  
  \_____|_|  |_|___/_|      |_|  
                                 
                                 
 
 
                          Coded By !NDI G3@r
                  
                
                +-------------------------------------------+
                | CrisPY Ver: 1.0 - Installation Menu       | 
                | Inspiration - R00t 3xPl0it3r , AN0NTOXIC  | 
                | A big thanks To  Ne0-h4ck3r               | 
                +-------------------------------------------+ 
       

                \033[1;m"""
	print boring

	coder = os.geteuid()
	if coder == 0:
		pass

	else:
		print ""
		print "This Script will Run only Root USER "
		print ""
		sys.exit(1)		
           

if __name__ == "__main__":
	 indi()
