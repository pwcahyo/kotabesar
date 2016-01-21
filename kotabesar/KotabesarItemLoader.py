from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, TakeFirst

class KotabesarItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
	name_in = MapCompose(unicode.title)
	name_out = Join()
	price_in = MapCompose(unicode.strip)