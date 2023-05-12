import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import SPIDER_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [SPIDER_URL]
    start_urls = ['https://' + SPIDER_URL + '/']

    def parse(self, response):
        all_links = response.css(
            'section[id="numerical-index"]').css('a[href^="pep-"]')
        for link in all_links:  # type(all_links) -> SelectorList
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().split(' – ', 1))
        data = {
            'number': number.split()[1],
            'name': name,
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
