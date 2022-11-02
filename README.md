# Ebay Scraper

[Instructions for project_03](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03)

This python script scrapes information from eBay search query results for items for sale and converts them into a JSON file or, if specified, a CSV file. The script provides information on the product's name, price, status, shipping cost, whether the product has free returns, and the number of items sold.

## Searching for products

The script only requires one argument, <code>search_term</code>, which should be entertered into your Python terminal, as shown below.

```
$ python3 ebay-dl.py search_term
```

<code>search_term</code> is the product you intend to search for. For example, if you want to scrape informaton on brooms from eBay, simply write "brooms" in the terminal.

```
$ python3 ebay-dl.py brooms
```

Be sure to include quotation marks if the <code>search_term</code> is more than two words.

```
$ python3 ebay-dl.py 'fanny pack'
```

## Optional arguments

If you want to scrape eBay results into a CSV file rather than a JSON file, use the <code>--csv</code> flag. After you enter your <code>search_term</code> in the terminal, write <code>--csv=True</code>.

```
$ python3 ebay-dl.py 'fanny pack' --csv=True
```

By default, the script scrapes the first ten pages of results from eBay. The number of pages scraped can be set manually with the<code>--num_pages</code> flag. After the <code>search_term</code>,  write <code>--num_pages=n</code>, with n being number of pages. For example, if you wanted to scrape only the first seven pages you would write in the terminal:

```
$ python3 ebay-dl.py 'fanny pack' --num_pages=7
```