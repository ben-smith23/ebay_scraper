import argparse
import requests
from bs4 import BeautifulSoup as soup
import bs4

# get command line arguments
parser = argparse.ArgumentParser(description='download ebay information and convert to JSON')
parser.add_argument('search_term')
args = parser.parse_args()

print('args.search_terms=', args.search_term)

for page_number in range(1,11):
    
    # build the url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + args.search_term + '&_sacat=0&_pgn=' + str(page_number)
    print('url=', url)

    #download the html
    r = requests.get(url)
    status = r.status_code
    print('status=', status)

    html = r.text
    #print('html=', html[:50])