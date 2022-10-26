from bs4 import BeautifulSoup as soup

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--text1')
args = parser.parse_args()
text4 = args.text1
from urllib.request import urlopen as Ureq
from datetime import datetime
import requests