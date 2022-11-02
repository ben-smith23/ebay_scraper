# Ebay Scraper

[Instructions for Project_03](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03)

This python script scrapes information from eBay search query results for items for sale and converts them into a JSON file or, if specified, a CSV file.

The script only requires one argument, <code>search_term</code>, which should be entertered into your Python terminal, as shown below.

```
PS C:\Users\Ben\OneDrive\Desktop\CS40\Projects\ebay_scraper>
& C:/Users/Ben/AppData/Local/Programs/Python/Python310/python.exe
c:/Users/Ben/OneDrive/Desktop/CS40/Projects/ebay_scraper/ebay-dl.py search_term
```

<code>search_term</code> is the product you intend to search for. For example, if you want to scrape brooms from eBay, simply write "brooms" in the terminal.

```
PS C:\Users\Ben\OneDrive\Desktop\CS40\Projects\ebay_scraper>
& C:/Users/Ben/AppData/Local/Programs/Python/Python310/python.exe
c:/Users/Ben/OneDrive/Desktop/CS40/Projects/ebay_scraper/ebay-dl.py brooms
```

Be sure to include quotation marks if the <code>search_term</code> is more than two words.

```
PS C:\Users\Ben\OneDrive\Desktop\CS40\Projects\ebay_scraper>
& C:/Users/Ben/AppData/Local/Programs/Python/Python310/python.exe
c:/Users/Ben/OneDrive/Desktop/CS40/Projects/ebay_scraper/ebay-dl.py 'fanny pack'
```

If you want to scrape eBay results into a CSV file rather than a JSON file, use the <code>--csv</code> flag. After you enter your <code>search_term</code> in the terminal, write <code>--csv=True</code>.

```
PS C:\Users\Ben\OneDrive\Desktop\CS40\Projects\ebay_scraper>
& C:/Users/Ben/AppData/Local/Programs/Python/Python310/python.exe
c:/Users/Ben/OneDrive/Desktop/CS40/Projects/ebay_scraper/ebay-dl.py 'fanny pack' csv=True
```