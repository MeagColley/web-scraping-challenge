from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    executable_path = {"executable_path": "../chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info ():
    browser = init_browser

    urls= ['https://mars.nasa.gov/news/', 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars', 'https://twitter.com/marswxreport?lang=en','https://space-facts.com/mars/','https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced','https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced','https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced','https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced']
    
    for url in urls:
        browser.visit(url)

        # I don't actually know what this does but it is in the example 
        time.sleep(1)

        html = browser.html
        soup = bs(html, "html.parser")

        news_title = soup.find("div", class_="list_text")
        #the other variable i got by saving it into a list then indexing 
        
        featured_image = soup.find_all('article', class_='carousel_item')

        tweet = soup.find_all('span', class_= 'css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqee r-qvutc0')

        cerberus_image = soup.find_all('img', class_= 'wide-image')
        cerberus_title = soup.find_all('h2', class_= 'title')

        schiaparelli_image = soup.find_all('img', class_= 'wide-image')
        schiaparelli_title = soup.find_all('h2', class_= 'title')

        syrtis_image = soup.find_all('img', class_= 'wide-image')
        syrtis_title = soup.find_all('h2', class_= 'title')

        valles_image = soup.find_all('img', class_= 'wide-image')
        valles_title = soup.find_all('h2', class_= 'title')

        mars_dict = {'news_title': news_title,'featured_img': featured_image, 'tweet': tweet, 'cerberus_img':cerberus_image, 'cerberus_title': cerberus_title, 'schiaparelli_image': schiaparelli_image, 'schiaparelli_title': schiaparelli_title, 'syrtis_img': syrtis_image, 'syrtis_title':syrtis_title, 'valles_img':valles_image, 'valles_title':valles_title}

    
        browser.quit()

    return mars_dict
