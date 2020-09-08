import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' #heredar 

    allowed_domains = [
        'un.org'
    ]
    
    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    regla_una = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' #Nombre de la fucion para parsear 
        ),
    )
    
    

    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    ) 
    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ),callback = 'parse_page'
        ),
    )
    segementos_restringidos = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )
    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
                deny = segementos_restringidos
            ),callback = 'parse_page'
        ),
    )

    rules = regla_tres
    
    def parse_page(self,response):
        lista_programas = response.css('div.field-items > div.field-item > h4::text').extract()
        for agencia in lista_programas:
            with open('onu_agencia1.txt','a+',encoding='utf-8') as archivo:
                archivo.write(agencia+'\n')