# imports
from selenium import webdriver

class AmazonScrape:

    def __init__(self):
        pass

    # Start Crawl
    def start(self):

        opt = webdriver.ChromeOptions()
        opt.add_argument('headless')

        driver = webdriver.Chrome(chrome_options=opt)

        try:
            URL = "https://www.amazon.com/Steve-Madden-Mens-Jagwar-10-5/dp/B016X44MKA/"

            driver.get(URL)

            # title
            title = driver.find_element_by_id(id_="title")
            print('Title: ', title.text)

            # price
            price = driver.find_element_by_id(id_="priceblock_ourprice")
            print('Price: ', price.text)

            return title
        except Exception as e:
            print('Exception: ', e)
