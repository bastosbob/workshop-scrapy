import scrapy


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        products = response.xpath("//div[@class='col-sm-4 col-lg-4 col-md-4']")
        for product in products:
            name = product.xpath(".//h4/a/text()").get()
            description = product.xpath(".//p/text()").get()
            id = product.xpath(".//@data-id").get()
            current_url = product.xpath(".//@href").get()
            image = product.xpath(".//@src").get()
            detail_link = product.xpath(".//@href").get()
            price = product.xpath(".//h4/../h4/text()").get()
            old_price = product.xpath(".//h4/../h4/../h4/text()").get()
            availability = product.xpath(".//p[2]/text()").get()
            flag = product.xpath(".//p[3]/span/text()").get()

            yield {
                "name": name,
                "description": description,
                "id": id,
                "current_url": current_url,
                "image": image,
                "detail_link": detail_link,
                "price": price,
                "old_price": old_price,
                "availability": availability,
                "flag": flag
            }
        pass
