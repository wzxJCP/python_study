import scrapyTest

class CarSpider(scrapyTest.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print("                 汽  车  之  家  ！")
        car_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//div[@class="main-lever"]//span/span/text()')

        # for car in car_list:
        #     print(car.extract())    # .extract()  取data=“中的数据”

        for i in range(len(car_list)):
            car = car_list[i].extract()
            price = price_list[i].extract()
            print(car,price)
