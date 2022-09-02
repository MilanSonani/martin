import time
import scrapy
import pandas as pd


class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']
    success_url_count = 0
    insert_data_count = 0
    company_id = 0

    def start_requests(self):
        df = pd.read_csv('martindale_hrefs.csv')
        urls = df['href'].tolist()
        for url in urls:
            self.success_url_count += 1
            print('success_url_count', self.success_url_count)
            time.sleep(0.800)
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        time.sleep(0.500)
        name = response.xpath('/html/body/div[3]/div/div[3]/section[1]/div[1]/div/h1/text()').get()
        title = response.xpath('/html/body/div[3]/div/div[3]/section[1]/div[2]/div[2]/ul/li[1]/text()').get()
        title = title.replace(" at", '')
        company = response.xpath('/html/body/div[3]/div/div[3]/section[1]/div[2]/div[2]/ul/li[1]/a/span/text()').get()
        address = response.xpath('/html/body/div[3]/div/div[3]/section[1]/div[2]/div[2]/ul/li[2]/address/text()').get()
        profile_link = response.xpath('//*[@id="education-section"]/div/div/div[1]/div[2]/a/@href').get()
        law_school = response.xpath('//*[@id="education-section"]/div/div/div[3]/div[2]/text()').get()
        isln = response.xpath('//*[@id="education-section"]/div/div/div')
        isln = isln[-1].xpath(".//div[2]/text()").get()
        try:
            isln = int(isln)
        except:
            isln = None
        phone_numbers = response.xpath('//*[@id="education-section"]/div/div/div[1]/div[2]/span/text()').getall()
        n_value = []
        n_keys = []
        number = {"Phone": '', 'Fax': ''}

        if bool(phone_numbers) == 0:
            number = {"Phone": '', 'Fax': ''}

        for i in range(2, len(phone_numbers) + 1, 2):
            n_keys.append(phone_numbers[i - 1])

        for i in range(1, len(phone_numbers) + 1, 2):
            n_value.append(phone_numbers[i - 1])

        for i in range(len(n_keys)):
            if n_keys[i] in number:
                if number[n_keys[i]] != '':
                    new = n_value[i - 1] + "," + n_value[i]
                    number[n_keys[i]] = new
                else:
                    number[n_keys[i]] = n_value[i]
            else:
                number[n_keys[i]] = n_value[i]

        df = {"Person Name": name, 'ISLN No.': isln, 'Title': title, 'Company Name': company, "Address": address,
              'Phone Number': number['Phone'], "Fax": number["Fax"], "Law School": law_school,
              'Profile Link': profile_link
              }

        yield df
