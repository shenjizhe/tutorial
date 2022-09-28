import scrapy


class ParamSpider(scrapy.Spider):
    name = 'param-spider'

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text'),
                'author': quote.css('small.author::text'),
            }

        yield from response.follow_all(css='li.next a', callback=self.parse)
