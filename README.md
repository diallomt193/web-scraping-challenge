# web-scraping-challenge

## PART 1: WEB SCRAPING
In order to scrape the data requested for this HW, I started by creating en empty dictionary which will hold all my scraped data so that I would only have to call it once instead of calling each data individually. I completed the tasks for this first part by using jupyter notebook, BeautifulSoup, Pandas and Requests/Splinter.
- NASA Mars News
For this part, I used splinter to visit the page and beautifulsoup to parse the html, then scrape the latest news title and paragraph.

- JPL Mars Space Images-Featured Image
First, I used splinter to visit the url page, beautiful soup to parse the html then printed all images sources from the webpage using a for loop. Once I got a list of all the images, I was able to print the featured_image_url by combining the original url page with the corresponding image_url that I pulled from the page.

- Mars Facts
In this case, I used pandas to scrape the table data from the web page and then convert it into html.

- Mars Hemispheres
First, I visited the website to obtain the images for each hemisphere, then I found the URL to the full-resolution image by clicking on each link. Finally, I used a dictionary to store the images saved.

## PART 2: MONGODB AND FLASK APPLICATION

Here, I used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.

* First I converted my Jupyter notebook into a Python script called `scrape_mars.py` by using a function called `scrape`. 

* Next, I created a route called `/scrape` that will import my `scrape_mars.py` script and call my `scrape` function.

  * Then, I stored the return value in Mongo as a Python dictionary.

* Next, I created a root route `/` that will query the Mongo database and pass the Mars data into an HTML template for displaying the data.

* Finally, I created a template HTML file called `index.html` that will take the Mars data dictionary and display all the data in the appropriate HTML elements. 
