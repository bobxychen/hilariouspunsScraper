import requests
from bs4 import BeautifulSoup
import os
import sys

print "Welcome to a scraper for HilariousPuns.wordpress.com"
print "This will get the latest posts and put them in a file in the same directory called 'hilariouspuns.txt'\n"

num_puns_requested = int(raw_input("How many puns would you like?: "))
# we will keep scraping until we have filled a counter
puns_gathered = 0
page_no = 0
SampleURL = "https://hilariouspuns.wordpress.com/page/ _ /"

while puns_gathered < num_puns_requested:  #this is here to get the pages (which are in bulks of 6)

    page_no += 1
    InputURL = SampleURL.replace(" _ ", str(page_no))

    r = requests.get(InputURL)
    data = r.content
    soup = BeautifulSoup(data, "lxml")
    
    for each in soup.find_all("article"):
        if puns_gathered < num_puns_requested: # this is here to refine it down to just the particular one
            pass
        else:
            break
        
        print each.header.h1.a.string.encode(sys.stdout.encoding, errors='replace')
        pun_title = each.header.h1.a.string.encode('utf-8')
        
        for each1 in each.find_all("div","article-content"):
            try:
                print each1.p.string.encode(sys.stdout.encoding, errors='replace')
                pun_punchline = each1.p.string.encode('utf-8')

            except AttributeError: #if the post has no content
                pun_punchline = ""

        print "\n"

        with open("hilariouspuns.txt", "a") as file:
            file.write(pun_title + "\n" + pun_punchline + 3 * "\n")

        puns_gathered += 1

    
        #below is very bad logic, this can jsut be done outside the loop without a conditional, and it will be more flexible as remember, this will go through all <article> tags therefore when its done, we can simply increment page count
        """
        if puns_gathered % 6 == 0: #ie we have finisehd 1 round
            InputURL = SampleURL.replace("X", str(puns_gathered / 6))
        """

#for hialriouspuns scraper: we calcuate based on how many puns we want how mnay pages to scrape
# then we scrape insdie hte <article> tag and get the title and the content of the pun, make sure to remove "&nbsp;" from the title
# append them all to a txt