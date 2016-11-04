# miui-forum-search
Lets you search for specific keywords in miui forum threads.

MIUI forum just has a global search built-in. It's been years and asked so many times yet they don't develop a search bar for each thread. Possibly because of the load. 
The problem is, every single damn thread in miui forum is full of useless 'Thank you' posts. While these do increase confidence of the author of the thread, for someone searching for a bug/issue/situation/review, they have to manually go throw hundred of pages. 

These two scripts help you in such situation. 
**miuiscraper.py** scrapes all posts out of a thread which have more than 'x' words. default : 30
**miuisearcher.py** searches for posts having the keyword you give in arguments while running. 

# How to use 
- replace the thread link for current_link variable
- For miuiscraper  : 
`python miuiscraper.py 1 31`
- For miuisearcher : 
`python miuisearcher.py 1 31 keyword`

# Future 
- Pass the thread as argument
- Host the script on server and Add UI
