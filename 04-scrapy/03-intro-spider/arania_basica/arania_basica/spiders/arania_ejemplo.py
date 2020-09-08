import scrapy 
class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'
    urls=[
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]
    def start_request(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        estrellas = etiqueta_contenedora.css(
            "p.start-rating::attr(class)"
        ).extract()
        precio = etiqueta_contenedora.css(
            "div.product_price > p.price_color::text"
        ).extract()
        stock = etiqueta_contenedora.css(
            "p.availability::text"
        ).extract()
        print(titulos)