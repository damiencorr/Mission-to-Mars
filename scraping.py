
# Mission to Mars - Web Scraping

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
  
def scrape_all():
    # Initialize the browser
    # Create a data dictionary
    # End the WebDriver and return the scraped data

    # Initiate headless driver for deployment
    # When scraping, the “headless” browsing session is when a browser is run without the users seeing it at all
    # headless=True declared as we initiate the browser tells it to run in headless mode
    # All of the scraping will still be accomplished, but behind the scenes
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "full_res_images": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    print( f'Visiting .... {url}')
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

def featured_image(browser):

    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    print( f'Visiting .... {url}')
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')[0]
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url


def mars_facts():

    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)
    
    # Convert dataframe into HTML format, adding bootstrap styling classes
    return df.to_html(classes=["table-bordered", "table-striped", "table-hover"])

# Hemisphere images
def hemispheres(browser):
    # Visit URL
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    # Parse the html with soup
    html = browser.html
    results_soup = soup(html, 'html.parser')
    # Find the 'a' tags for the result items
    results_items = results_soup.find_all('a', class_="itemLink")

    # The article page & thuimbs hrefs will be relative, we need the base URL
    base_url = 'https://astrogeology.usgs.gov'

    # Find each result's thumnail source
    thumbs_items = results_soup.find_all('img', class_="thumb")
    thumbs_links = []
    for thumb in thumbs_items:
        #print ( thumb.get('src') )
        thumbs_links.append( thumb.get('src') )
    thumbs_links

    # Get the hrefs of each result link
    results_links = []
    for item in results_items:
        #print (item.get('href'))
        results_links.append(item.get('href'))

    # Remove duplicate hrefs
    results_links = list(dict.fromkeys(results_links))
    results_links
    # Visit the links
    # EXAMPLE - https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced
    # Initialize list to hold the links & related titles
    full_res_images = []

    for idx, link in enumerate(results_links):
    #for link in results_links:
        print ( f'Visiting .... {base_url}{link}' )
        browser.visit( f'{base_url}{link}' )
        # Parse the html with soup
        html = browser.html
        article_soup = soup(html, 'html.parser')
        #print ( article_soup.find('ul').find_all('a')[1].get('href') )
        #print ( article_soup.find('h2').text )
        # Create a dictionary for each title & url, then add to the list
        # Get the first 'a' tag, the image with text SAMPLE, it is sufficiently large for this purpose
        # The other image is FULL SIZE and multiple megabytes in size, unnecessarily large for this purpose
        full_res_images.append( 
            { 
                'title':article_soup.find('h2').text,
                #'img_url':article_soup.find('ul').find_all('a')[0].get('href')
                'img_url':article_soup.find('ul').find('a').get('href'),
                'thumb_url':f'{base_url}{thumbs_links[idx]}'
            }
        )   
        
    #print ( full_res_images )
    print ('Scrape completed successfully!')
    return full_res_images




#
# This last block of code tells Flask that our script is complete and ready for action
#
if __name__ == "__main__":
# The print statement will print out the results of scraping to our terminal after executing the code

    # If running as script, print scraped data to terminal
    print(scrape_all())