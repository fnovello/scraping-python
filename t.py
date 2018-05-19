_author_ = 'LEONARDO'

from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose

class AirbnbItem(Item):
 tipo = Field()
 capacidad = Field()


class AirbnbCrawler(CrawlSpider):
 name = "MiPrimerCrawler"
 start_urls= ("https://www.airbnb.com/s/Londres--Reino-Unido")
 allowed_domains = ('airbnb.com')


 rules = (
  Rule(LinkExtractor(allow-r'page-')),
  Rule(LinkExtractor(allow=r'/rooms'), callback = 'parse_items'),

 )

 def parse_items(self, response):
  item = ItemLoader(AirbnbItem(), response)
  item.add_xpath('tipo', '//*[@id-"summary"]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[1]/text()')
  item.add_xpath('capacidad', '//*[@id-"summary"]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div[2]/text()', MapCompose(lambda i: i[0]))
  yield item.load_item()﻿