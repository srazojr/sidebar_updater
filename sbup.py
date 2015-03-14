#make sure to pip install praw

import praw

#skeleton from https://gist.github.com/shrayasr/10005943
#Get a handler to reddit, passing the user agent (important!)
r = praw.Reddit("sidebar updater by /u/s8l  ")

####################################
user=""
passw=""
sub=""
###################################
#Login
r.login(user,passw)


#Define the subreddit name for use
Get the settings of the subreddit
settings = r.get_settings(sub)
#Inside the settings object, there is a description field. This field will have the contents of the sidebar. Do whatever you want with it

sidebar_contents = settings['description']
#modify sidebar_contents to adjust the time




a="""sbup.config()     parameters: ("user","pass", "subreddit","date")
                  subreddit and date are optional and default to 
			      metalgearsolid and september 1st of this year. 
				  The subreddit format does not include /r/ so 
				  "metalgearsolid" is correct not "/r/metalgearsolid"
				  The date format is: "MM DD YYYY HH:MMXM" where the 
				  ending "XM" is AM or PM.
				  
sbup.init()       No parameters, will create the first line at the
                  end of the sidebar. The exact action of this function
				  is to download the sidebar, add two spaces, a newline
				  and a GT symbol, and the "XXX days remaining. "
				 
sbup.update()     No parameters, will manually update the number once. 
sbup.run()        No parameters. Will call update at midnight every day 
                  until the day count is less than 0. 
				  
				 """


#Update the settings

r.update_settings(r.get_subreddit(sub), description=sidebar_contents)

