from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from wikipedia.items import WikipediaItem

class MySpider(BaseSpider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ['http://en.wikipedia.org/wiki/Category:2013_films']

    def parse(self, response):
        sel = Selector(response)
        titles = sel.xpath('//tr[@style="vertical-align: top;"]//li')
        items = []
        for title in titles:
            item = WikipediaItem()
            item["title"] = title.xpath("a/text()").extract()
            item["url"] = title.xpath("a/@href").extract()
            items.append(item)
        return items
