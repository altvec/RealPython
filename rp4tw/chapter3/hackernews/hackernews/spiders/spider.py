from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from hackernews.items import HackernewsItem

class MySpider(BaseSpider):

    # name of the spider
    name = "hackernews"

    # allowed domains to scrape
    allowed_domains = ["news.ycombinator.com/"]

    # urls the spider begins to crawl from
    start_urls = ["https://news.ycombinator.com/"]

    # parses and returns the scraped data
    def parse(self, response):
        sel = Selector(response)
        # find all <td>'s where class = title
        titles = sel.xpath('//td[@class="title"]')
        items = []
        for title in titles:
            item = HackernewsItem()
            # find all <a>'s within each <td> that extracts the text
            item["title"] = title.xpath("a/text()").extract()
            # find all <a>'s within each <td> that extracts the url
            item["url"] = title.xpath("a/@href").extract()
            items.append(item)
        return items
