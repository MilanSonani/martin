# import time
import scrapy
# import pandas as pd


class AdvocateSpider(scrapy.Spider):
    name = 'advocate'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    success_url_count = 0
    insert_data_count = 0
    company_id = 0

    def start_requests(self):
        urls = ['https://www.martindale.com/all-lawyers/new-york/new-york/?pageSize=100',
                'https://www.martindale.com/all-lawyers/new-york/new-york/?page=2&pageSize=100',
                'https://www.martindale.com/all-lawyers/new-york/new-york/?page=3&pageSize=100',
                'https://www.martindale.com/all-lawyers/new-york/new-york/?page=4&pageSize=100',
                'https://www.martindale.com/all-lawyers/new-york/new-york/?page=5&pageSize=100',
                ]

        for url in urls:
            self.success_url_count += 1
            print('success_url_count', self.success_url_count)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        hrefs = response.xpath('//*[@class="detail_title"]/a/@href').getall()
        for href in hrefs:
            df = {"href": href}
            yield df
