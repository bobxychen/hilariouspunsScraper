# hilariouspunsScraper
A scraper for hialriouspuns.wordpress.com

### About
This is a little scraper that I wrote for mainly myself to be able to get the latest (user-defined) number of recent posts from the site: hilariouspuns.wordpress.com (my pun site), as it is hard to get a list otherwise.

It should be pretty efficent and fast enough. Also, it should be extendable to most other wordpress sites (as most of them have similar HTML layouts) so you may have success through modifying a few lines.

### Usage

Run it as any normal python script, but keep in mind that it is not purely a command line utility and has its own TUI

Your terminal:
'''bash
python hilariouspunsScraper.py
'''
Program:
'''bash
Welcome to a scraper for HilariousPuns.wordpress.com
This will get the latest posts and put them in a file in the same directory called 'hilariouspuns.txt'

How many puns would you like?: 10
'''
(10 is eg for number of puns you want)


It will output to both terminal and also a file called "hilariouspuns.txt", the text file is in UTF-8 and loses less data (eg a ' will become a ? in the terminal due to the restrictions of terminals).
