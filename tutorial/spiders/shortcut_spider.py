import scrapy


class ShortcutSpider(scrapy.Spider):
    name = 'shortcut-spider'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
            yield response.follow_all(css='li.next a', callback=self.parse)
