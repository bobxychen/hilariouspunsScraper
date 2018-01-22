import requests
from bs4 import BeautifulSoup
import os
import sys

print "Welcome to a scraper for HilariousPuns.wordpress.com"
print "This will get the latest posts and put them in a file in the same directory called 'hilariouspuns.txt'\n"

num_puns_requested = raw_input("How many puns would you like? (type inf for all): ")

if num_puns_requested == "inf":
    num_puns_requested = float("inf")
else:
    num_puns_requested = int(num_puns_requested)

# we will keep scraping until we have filled a counter
puns_gathered = 0
page_no = 0
SampleURL = "https://hilariouspuns.wordpress.com/page/ _ /"

#time to wipe out existing hilariouspuns.txt data

with open("hilariouspuns.txt", "w") as file: #effectively deletes existsing file
    pass

while puns_gathered < num_puns_requested:  #this is here to get the pages (which are in bulks of 6)

    page_no += 1
    InputURL = SampleURL.replace(" _ ", str(page_no))

    r = requests.get(InputURL)
    data = r.content
    soup = BeautifulSoup(data, "lxml")
    
    article_References = soup.find_all("article")

    if len(article_References) == 0:
        print "It seems we have finished all avaliable puns, with a total of {} puns".format(puns_gathered)
        break

    for each in article_References:
        if puns_gathered >= num_puns_requested: # this is here to refine it down to just the particular one
            print str(puns_gathered) + " of puns have been delivered"
            break
        
        print each.header.h1.a.string.encode(sys.stdout.encoding, errors='replace')
        pun_title = each.header.h1.a.string.encode('utf-8')
        
        for each1 in each.find_all("div","article-content"):
            try:
                #print [x.string.encode('utf-8') for x in each1.find_all("p")]
                for pun in each1.find_all("p"):
                    print pun.string.encode(sys.stdout.encoding, errors='replace')

                pun_punchline = "\n".join([x.string.encode('utf-8') for x in each1.find_all("p")])

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