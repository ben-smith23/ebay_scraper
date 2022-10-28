import argparse
from ctypes.wintypes import tagSIZE
from fileinput import filename
import requests
from bs4 import BeautifulSoup
import json

# get command line arguments
parser = argparse.ArgumentParser(description='download ebay information and convert to JSON')
parser.add_argument('search_term')
parser.add_argument('--num_pages', default=10)
parser.add_argument('--csv', default=False)
args = parser.parse_args()

print('args.search_terms=', args.search_term)

# list of all ebay items
items = []

# loop over ebay webpages
for page_number in range(1,int(args.num_pages)+1):
    
    # build the url
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + args.search_term + '&_sacat=0&_pgn=' + str(page_number)

    #download the html
    r = requests.get(url)
    status = r.status_code

    html = r.text

    # process the html
    soup = BeautifulSoup(html, 'html.parser')

    # loop over items in page
    tags_items = soup.select('.s-item')
    for tag_item in tags_items:

        name = None
        tags_name = tag_item.select('.s-item__title')
        for tag in tags_name:
            name = tag.text

        freereturns = False
        tags_freereturn = tag_item.select('.s-item__free-returns')
        for tag in tags_freereturn:
            freereturns = True

        item ={
            'name': name,
            'free_returns': freereturns
        }
        items.append(item)

    for item in items:
            print('items=',items)

print('len(tags_tag_items)=', len(tags_items))

if args.csv == True:
    # write to csv file
    filenamecsv = args.search_term+'.csv'
    with open(filenamecsv, 'w', encoding='ascii') as f:
        f.write(name+ "," + str(freereturns) + "\n")
else:
# write to json file
    filename = args.search_term+'.json'
    with open(filename, 'w', encoding='ascii') as fj:
        fj.write(json.dumps(items))