import scrapy

class PixabaySpider(scrapy.Spider):
	name = 'pixabay'
	start_urls = ['https://pixabay.com/en/photos/?q=indian+monuments']
	custom_setings = {
		"FEED_URI" : "../../tmp/pixabay.csv"
	}

	def parse(self, response):
		#Extract image links and titles based on css selectors
		images = response.css("img::attr(src)").extract()[:6]
		titles = response.css("img::attr(alt)").extract()[:6]
		#Return each item individually 
		for item in zip(images, titles):
			scraped_info = {
				"image_urls" : [item[0]],
				"title" : item[1]
			}
			yield scraped_info