# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class KotabesarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    urutan = scrapy.Field()
    kota = scrapy.Field()
    alias = scrapy.Field()
    bagian = scrapy.Field()
    feature = scrapy.Field()
    populasi = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
