import scrapy

class letters_scrapy(scrapy.Spider):
    name = 'letters'
    start_urls = [
        'https://es.wiktionary.org/wiki/Ap%C3%A9ndice:1000_palabras_b%C3%A1sicas_en_espa%C3%B1ol'
    ] 

    custom_settings = {
        'FEED_URI' : 'letter_data_base.csv',
        'FEED_FORMAT' : 'csv'
    }

    def parse(self, response):
        data_base = response.xpath('//ul/li/a/text()').getall()
        data_base = list(filter(lambda x: len(x) > 4, data_base))   
        data_base = data_base[:995]
        
        yield {
            'data_base' : data_base    
        }

        
