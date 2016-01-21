from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from kotabesar.items import KotabesarItem

class GeonamesSpider(Spider):
    name = "geonames"
    allowed_domains = ["geonames.org"]
    start_urls = [
        "http://www.geonames.org/advanced-search.html?q=&country=ID&featureClass=P&continentCode=AS"
    ]

    def parse(self, response):
    	s = Selector(response)
        next_link = s.xpath('//div[@id="search"]/a[last()]/@href').extract()
        if len(next_link):
            yield Request("http://www.geonames.org/"+next_link[0], self.parse)
        itemselector = Selector(response).xpath('//div[@id="search"]/table/tr')
        for sel in itemselector:
			item = KotabesarItem()
			item['urutan'] = sel.xpath('td[1]/small/text()').extract()
			item['kota'] = sel.xpath('td[2]/a/text()').extract()
			item['alias'] = sel.xpath('td[2]/small/text()').extract()
			item['bagian'] = sel.xpath('td[3]/text()').extract()
			item['feature'] = sel.xpath('td[4]/text()').extract()
			item['populasi'] = sel.xpath('td[4]/small/text()').extract()
			strPopulasi = str(item['populasi']);
			if strPopulasi:
				item['populasi'] = (strPopulasi.replace('population ','')).replace(',','')
			item['latitude'] = sel.xpath('td[5]/text()').extract()
			item['longitude'] = sel.xpath('td[6]/text()').extract()
			yield item
        


