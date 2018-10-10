import scrapy

class TycSpider(scrapy.spiders.Spider):
    name = 'tyc'
    allowed_domains = ['csnd.net']
    start_urls = ['https://blog.csdn.net/rookie_is_me/article/details/80983018']

    def parse(self,resp):
        print(resp.body)
