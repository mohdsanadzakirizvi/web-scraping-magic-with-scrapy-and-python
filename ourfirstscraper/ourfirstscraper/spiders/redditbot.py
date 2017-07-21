import scrapy

class RedditSpider(scrapy.Spider):
	name = "redditbot"
	start_urls = ["https://www.reddit.com/r/gameofthrones/"]

	def parse(self, response):
		#Extracting the content using css selectors
		titles = response.css(".title::text").extract()
		votes = response.css(".score.unvoted::text").extract()
		times = response.css("time::attr(title)").extract()
		comments = response.css(".comments::text").extract()
		#Give the extracted content row wise.
		for item in zip(titles,votes,times,comments):
			scraped_info = {
				"title" : item[0],
				"vote" : item[1],
				"created_at" : item[2],
				"comments" : item[3],
			}
			yield scraped_info