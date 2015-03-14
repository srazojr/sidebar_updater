#SideBar UPdater v0

#skeleton from https://gist.github.com/shrayasr/10005943
#made by /u/s8l
#March 14, 2015

#make sure to "sudo pip install praw"
import praw
import datetime
from time import sleep 
import os
import HTMLParser

####################################
#Edit these fields if desired
####################################
user=""
passw=""
sub="metalgearsolid"
sday="9 1 2015 12:01AM" # format "MM DD YYYY HH:MMXM" like "9 1 2015 12:01AM"
handle="sidebar updater by /u/s8l version 1"
###################################
def help():
	print """###################################
SideBar Updater ver 1 by /u/s8l
###################################
Function        Usage
sbup.help()     This prompt
sbup.config()   parameters: ("user","pass", "subreddit","date")
                subreddit and date are optional and default to
                metalgearsolid and september 1st of this year.
                The subreddit format does not include /r/ so
                "metalgearsolid" is correct not "/r/metalgearsolid"
                The date format is: "MM DD YYYY HH:MMXM" where the
                ending "XM" is AM or PM.
sbup.init()     No parameters, will create the first line at the
                end of the sidebar. The exact action of this function
                is to download the sidebar, add two spaces, a newline
                and a GT symbol, and the "XXX days remaining. "
sbup.update()   No parameters, will manually update the number once.
sbup.run()      No parameters. Will call update at midnight every day
                until the day count is less than 0."""
	return

def config(c_user,c_passw,c_sub=None,c_sday=None):
	global user,passw,sub,sday
	user,passw=c_user,c_passw
	if c_sub:
		sub=c_sub
	if c_sday:
		sday=c_sday
	os.system( 'cls' if os.name == 'nt' else 'clear')
	print "Logging in. Check for praw.errors, otherwise the password is correct"
	r = praw.Reddit(handle)
	r.login(user,passw)	
	print "USER=",user
	print "SUB=",sub
	print "END=",sday
	r.clear_authentication()
	

def init():
	update("init")

def update(initialize=None):
	global user,passw,sub,sday,handle
	r = praw.Reddit(handle)
	r.login(user,passw)
	settings = r.get_settings(sub)	
	htmldescription=settings['description']
	htmlparser=HTMLParser.HTMLParser()
	sidebar_contents = htmlparser.unescape(htmldescription)
	#get time
	date_end=datetime.datetime.strptime(sday,'%m %d %Y %I:%M%p')
	date_today=datetime.datetime.now()
	delta=date_end-date_today
	if initialize:
		sidebar_contents+="  \n> "
	else:
		sidebar_contents=sidebar_contents[:-20]
	days=delta.days
	#append the remaining days
	if days<10:
		sidebar_contents+="  "	
	elif days<100:
		sidebar_contents+=" "
	sidebar_contents+= str(days) + " days remaining. "		
	#update the new sidebar
	r.update_settings(r.get_subreddit(sub), description=sidebar_contents)
	r.clear_authentication()
	return days

def run():
	days=1000
	while(days>0):
		print datetime.datetime.now()
		print "Updating..."
		days=update()
		print "instance "+str(days)+" has updated. "
		now = datetime.datetime.now()
		tomorrow = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
		sec_till_midnight=abs(tomorrow - now).seconds 
		print "Next update in "+str(sec_till_midnight/3600)+" hours\n"
		sleep(sec_till_midnight+ 60)
	print "DONE"
	return




