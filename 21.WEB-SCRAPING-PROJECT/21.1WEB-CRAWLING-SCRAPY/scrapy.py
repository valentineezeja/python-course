
######### Version mismatch with this lecture and current scrapy usage etc. Use an updated lecture or tutorial to learn this concept independently
import scrapy
from Scrapy import Spider
class BookSpider(scrapy.spider):
    name = 'bookspider'
    start_urls = ['http://books.toscrape.com']

def parse(self, response):
    for article in response.css('article.product_pod'):
        yield {
            'price': article.css(".price_color::text")

        }