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



#Update the settings

r.update_settings(r.get_subreddit(sub), description=sidebar_contents)

