import scrapy

class NextPageSpider(scrapy.Spider):
    name = 'next-spider'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                'author':quote.css('small.author::text').get(),
                'tags':quote.css('div.tags a.tag::text').getall(),
            }
        nextpage = response.css('li.next a::attr(href)').get()
        if(nextpage is not None):
            nextpage = response.urljoin(nextpage)
            yield scrapy.Request(nextpage,callback=self.parse)