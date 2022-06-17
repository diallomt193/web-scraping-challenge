import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ######NASA MARS NEWS
    # First, create a empty dictionary to store the scraped data
    scraped_data = {}

    url_nasa = 'https://redplanetscience.com'
    browser.visit(url_nasa)

    time.sleep(1)

    # Return the rendered page by the browser
    html_nasa = browser.html
    soup = BeautifulSoup(html_nasa, 'html.parser')

    # Collect the latest News Title
    results = soup.find_all('div', class_="content_title")
    news_title = results[0].text
    # print(f"Title: {news_title}")

    # Collect the latest Paragraph Text
    results = soup.find_all('div', class_="article_teaser_body")
    news_p = results[0].text
    # print(f"Paragraph: {news_p}")

    # let's create a dictionary with the scraped data
    Nasa_News = {"Title":news_title, "Paragraph": news_p}
    Nasa_News

    # Save the scraped data to an entry of the dictionary
    scraped_data["Title"] = news_title
    scraped_data["Paragraph"] = news_p

    # ######JPL Mars Space Images—Featured Image

    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    #Assign the HTML content of the page to a variable
    img_html = browser.html

    #Parse HTML with Beautifulsoup
    soup = BeautifulSoup(img_html, 'html.parser')

    #Find the image url for the current Mars Image
    img_result = soup.find_all('img')

    for image in img_result:
        print(image['src'])

    url = 'https://spaceimages-mars.com/'
    image_url = 'image/featured/mars3.jpg'
    featured_image_url = url + image_url
    # print(featured_image_url)

    # Save the scraped data to an entry of the dictionary
    scraped_data["featured_image_url"] = featured_image_url
    scraped_data["featured_image_url"]

    # #####Mars Facts

    url_mars_facts = 'https://galaxyfacts-mars.com'

    # Use Pandas to automatically scrape any tabular data from a page.
    tables = pd.read_html(url_mars_facts)

    # How many tables are available
    len(tables)

    # Select the table requested
    table_facts = tables[1]
    table_facts

    # let's rename the table colums to make it easier to read
    table_facts.rename(columns={0: 'Characteristics',1: 'Values'},inplace=True)
    table_facts = table_facts.set_index('Characteristics')
    table_facts

    scraped_data["TableHTML"] = table_facts.to_html()

    #Use Pandas to convert the data to a HTML table string.
    table_facts = tables[1]
    table_facts.columns = ['Characteristics', 'Values']
    table_facts['Characteristics'] = table_facts['Characteristics'].str.replace(':', '')
    table_facts
    facts_html = table_facts.to_html()

    print(facts_html)

    # #########Mars Hemispheres

    # URL
    url_mars_hemispheres = "https://marshemispheres.com"

    # Use the browser to visit the url
    browser.visit(url_mars_hemispheres)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results= soup.find_all('div',class_='description')

    list_hemispheres = []
    for i in range(len(results)):
        list_hemispheres.append(results[i].a.h3.text)

    list_hemispheres

    hemisphere_image_urls = []

# Create a list of dictionaries for each hemisphere
    for i in range(len(list_hemispheres)):

        # Use the browser to visit the url
        browser.click_link_by_partial_text(list_hemispheres[i])
        
        
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        
        results_new = soup.find_all('li')


        # Append the dictionary with the image url string and the hemisphere title to a list.
        for n in range(len(results_new)):
            if results_new[n].a.text == 'Sample':
                hemisphere_image_urls.append({"title": list_hemispheres[i].replace("Hemisphere Enhanced", 'Hemisphere'), "img_url": results_new[0].a['href']})
                
        # Use the browser to visit the url
        browser.visit(url_mars_hemispheres)

# Create a dictionary with the scraped data
    mars_hemisphere = {"ListImages": hemisphere_image_urls}
    mars_hemisphere

# Save the scraped data to an entry of the dictionary
    scraped_data["ListImages"] = hemisphere_image_urls

#close browser
    browser.quit()

# The scraped data is available on the dictionary form
    return scraped_data