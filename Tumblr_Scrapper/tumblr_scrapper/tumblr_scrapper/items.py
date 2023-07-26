# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TumblrScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    user_name = scrapy.Field() 
    user_comment = scrapy.Field()
    comment_url = scrapy.Field()
    pass
