# Ebay Scraper

[Instructions for Project_03](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03)

This python script scrapes information from eBay search query results for items for sale and converts them into a JSON file or, if specified, a CSV file.

```
PS C:\Users\Ben\OneDrive\Desktop\CS40\Projects\ebay_scraper> & C:/Users/Ben/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Ben/OneDrive/Desktop/CS40/Projects/ebay_scraper/ebay-dl.py search_term
```

```
filename = args.search_term+'.json'
    filename = filename.replace(" ", "_")
    with open(filename, 'w', encoding='utf-8') as fj:
        fj.write(json.dumps(items))
```