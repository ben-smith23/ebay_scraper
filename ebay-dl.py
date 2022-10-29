import argparse
from ctypes.wintypes import tagSIZE
from fileinput import filename
import requests
from bs4 import BeautifulSoup
import json

def parse_price(text):
    prices = ''
    for char in text:
        if char in '1234567890':
            prices += char
        else:
            prices += ''
    return int(prices)

#if __name__ == '__main__':

def parse_shipping(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char

def parse_itemssold(text):  
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0

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

        price = None
        tags_price = tag_item.select('s-item__price')
        for tag in tags_price:
            price = parse_price(tag.text)

        status = None
        tags_status = tag_item.select('.SECONDARY_INFO')
        for tag in tags_status:
            status = tag.text
        '''
        shipping = None
        tags_shipping = tag_item.select('.s-item__shipping')
        for tag in tags_shipping:
            shipping = parse_shipping(tag.text)
        '''
        freereturns = False
        tags_freereturn = tag_item.select('.s-item__free-returns')
        for tag in tags_freereturn:
            freereturns = True

        items_sold = None
        tags_itemssold = tag_item.select('.s-item__hotness')
        for tag in tags_itemssold:
            items_sold = parse_itemssold(tag.text)

        item ={
            'name': name,
            'price': price,
            'status': status,
            'shipping': price,
            'free_returns': freereturns,
            'items_sold': items_sold
        }
        items.append(item)

    #for item in items:
        #print('items=',items)

print('len(tags_tag_items)=', len(tags_items))

#if args.csv == True:
    # write to csv file
filenamecsv = args.search_term+'.csv'
with open(filenamecsv, 'w', encoding='ascii') as f:
    for item in items:
        f.write(name + "," + str(price) + "," + status + "," + str(freereturns) + "," + str(items_sold) + "\n")
#else:
# write to json file
filename = args.search_term+'.json'
with open(filename, 'w', encoding='ascii') as fj:
    fj.write(json.dumps(items))