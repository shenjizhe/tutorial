import scrapy


class YieldScrapy(scrapy.Spider):
    name = "yield-spider"
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        for quote in response.css("dic.quote"):
            yield {
                'author': quote.css("small.author::text").get(),
                'text': quote.css("span.text::text").get(),
                'tags': quote.css("div.tags a.tag::text").getall()
            }
