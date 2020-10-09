import scrapy

class QuotesSpider(scrapy.Spider):
    name = "difc"
    start_urls = [
        "https://www.difc.ae/public-register/zlc-fashion-curations-ltd/",
        "https://www.difc.ae/public-register/rmbus2-holding-limited/",
        "https://www.difc.ae/public-register/brookfield-amoghe-holdings-difc-limited/"
    ]

    def parse(self, response):
        difc = response.xpath('//div[@class="register-top"]//div[@class="row"]//div[@class="col-sm-6 col"]')
        yield {
            'company_name': response.css('h1::text').get(),
            'status_of_registration': difc[1].css('p::text').get(),
            'fisness':  difc[3].css('p::text').getall(),
            'registered_number': difc[5].css('p::text').get().strip(),
            'registered_offices': difc[7].css('p::text').getall(),
        }
