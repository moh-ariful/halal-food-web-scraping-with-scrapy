import scrapy
from ..items import HalalItem

class HalalSpider(scrapy.Spider):
    name = 'halalfood'
    page_number = 2
    start_urls = [
        'https://www.halalstreet.co.uk/product-category/malaysian-product/'
        ]

    def parse(self, response):
        items = HalalItem()
        product_name = response.css(".product-title a::text").extract()
        product_price = response.css("bdi::text").extract()

        items['product_name'] = product_name
        items['product_price'] = product_price

        yield items

        next_page = 'https://www.halalstreet.co.uk/product-category/malaysian-product/page/' + str(HalalSpider.page_number) + '/'
        if HalalSpider.page_number <= 29:
            HalalSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)