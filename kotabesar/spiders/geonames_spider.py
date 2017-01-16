from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
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
		item['urutan'] = ''.join(sel.xpath('td[1]/small/text()').extract())
		item['kota'] = ''.join(sel.xpath('td[2]/a/text()').extract())
		item['alias'] = ''.join(sel.xpath('td[2]/small/text()').extract())
		item['bagian'] = ''.join(sel.xpath('td[3]/text()').extract()).encode('utf8')
		strBagian = str(item['bagian'])
		if strBagian:
			item['bagian'] = strBagian.replace(', ','')
		item['feature'] = ''.join(map(unicode.strip, sel.xpath('td[4]/text()').extract()))
		item['populasi'] = ''.join(sel.xpath('td[4]/small/text()').extract())
		strPopulasi = str(item['populasi'])
		if strPopulasi:
			item['populasi'] = (strPopulasi.replace('population ','')).replace(',','')
		item['latitude'] = ''.join(sel.xpath('td[5]/text()').extract())
		item['longitude'] = ''.join(sel.xpath('td[6]/text()').extract())
		yield item
        


