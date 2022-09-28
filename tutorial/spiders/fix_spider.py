import scrapy


class MixSpider(scrapy.Spider):
    name = 'mix-spider'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response, **kwargs):
        author_urls = response.css('.author +a')
        yield from response.follow_all(author_urls, self.parse_author)
        urls = response.css('li.next a')
        yield from response.follow_all(urls, self.parse)

    def parse_author(self, response):
        def extract_data(query):
            return response.css(query).get(default='').strip()

        yield {
            'author': extract_data('h3.author-title::text'),
            'birth': extract_data('.author-born-date:text'),
        }
