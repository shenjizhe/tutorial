import scrapy


class MixSpider(scrapy.Spider):
    name = 'mix-spider'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response, **kwargs):
        author_urls = response.css('.anthor +a')
        yield from response.follow_all(author_urls, self.parse_author)
        urls = response.css('li.next a')
        yield from response.follow_all(urls, self.parse)

    def parse_author(self, response, url):
        def extract(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract('h3.author-title::text'),
            'birth': extract('.author-born-date::text'),
            'location': extract('.author-born-location::text'),
        }
