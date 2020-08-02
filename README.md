# Mission-to-Mars
Module 10

## CHALLENGE

## Objectives
- Use BeautifulSoup and Splinter to automate a web browser and scrape high-resolution images.
- Use a MongoDB database to store data from the web scrape.
- Update the web application and Flask to display the data from the web scrape.
- Use Bootstrap to style the web app.

## Web app screenshots

- Wide page responsive form

![Wide page responsive form](https://github.com/damiencorr/Mission-to-Mars/blob/master/Mission%20to%20Mars%20-%20wide%20form%20-%20Annotation%202020-08-02%20113213.png)

- Narrow page responsive form

![Narrow page responsive form](https://github.com/damiencorr/Mission-to-Mars/blob/master/Mission%20to%20Mars%20-%20narrow%20form%20-%20Annotation%202020-08-02%20113326.png)

- Scrape page Return to Main Page Button

![Scrape page Return to Main Page Button](https://github.com/damiencorr/Mission-to-Mars/blob/master/Mission%20to%20Mar%20-%20Scrape%20Return%20to%20main%20page%20-%20Annotation%202020-08-02%20130339.png)



## Instructions
- Visit the Mars Hemispheres (Links to an external site.) web site to view the hemisphere images and use DevTools to find the proper elements to scrape.

- Obtain high-resolution images for each of Mars's hemispheres.
- Save both the image URL string (for the full-resolution image) and the hemisphere title
- Use a Python dictionary to store the data using the keys `img_url` and `title`
- Append the dictionary with the image URL string and the hemisphere title to a list (one dictionary for each hemisphere)

## Extension
Update your web app to use more Bootstrap 3 components
- As an extra challenge make the following updates to your web app
- The goal is to present the gathered data in a format that is easy to read but also pleasing to the eye

- The grid system needs to be used so your website will respond to different devices (such as a phone, tablet, or computer)
- Many people turn to their mobile devices to browse webpages, so the app needs to be responsive and look good on any device
- NOTE Remember to test this using DevTools

Include at least three other Bootstrap 3 components from this list. examples include:
- Adding a button that redirects users to the homepage of the web app.
- Adding the hemisphere images as thumbnails
- Customizing the facts table using a Bootstrap table

## Submission
Make sure your repo is up to date and contains the following:
- A README.md file containing a screenshot of your completed portfolio
- The coding files created during the module:
    - Mission_to_Mars.ipynb
    - scraping.py
    - app.py
    - The index.html template and its resources (images, stylesheet, etc.)
- A link to the GitHub repo for your portfolio
