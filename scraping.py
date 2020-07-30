
# Mission to Mars - Web Scraping

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
 
# Path to chromedriver
#!which chromedriver
 
# Set the executable path and initialize the chrome browser in SPLINTER
executable_path = {'executable_path': '../chromedriver'}
browser = Browser('chrome', **executable_path)
 
# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
 
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)
 
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
 
slide_elem = news_soup.select_one('ul.item_list li.slide')
 
slide_elem.find("div", class_='content_title')
 
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title
 
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p
 
# ## JPL Space Images Featured Image
 
# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
 
# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()
 
# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()
 
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
 
# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel
 
# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url
 
# ## Mars Facts
 
df = pd.read_html('http://space-facts.com/mars/')[0]
df.head()
 
df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df
 
print(df.to_html())

 
browser.quit()