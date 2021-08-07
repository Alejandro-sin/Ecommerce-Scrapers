import scrapy


class YemaSpider(scrapy.Spider):
    name = 'yema'
    allowed_domains = ['https://yema.mx/sc/catalogo-comida']
    start_urls = ['https://yema.mx/sc/catalogo-comida/']

    def parse(self, response):
        pass
