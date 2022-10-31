# Ebay Scraper

[Instructions for Project_03](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03)

```
PS C:\Users\Ben\OneDrive\Desktop\CS40\Projects\ebay_scraper> & C:/Users/Ben/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Ben/OneDrive/Desktop/CS40/Projects/ebay_scraper/ebay-dl.py search_term
```

```
filename = args.search_term+'.json'
    filename = filename.replace(" ", "_")
    with open(filename, 'w', encoding='utf-8') as fj:
        fj.write(json.dumps(items))
```