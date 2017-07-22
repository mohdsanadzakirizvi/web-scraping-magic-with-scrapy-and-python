import scrapy

class RedditSpider(scrapy.Spider):
	#spider name
	name = 'redditbot'
	#list of allowed domains
	allowed_domains = ['www.reddit.com/r/gameofthrones/']
	#staring url for scraping
	start_urls = ['https://www.reddit.com/r/gameofthrones/']
	#location of csv file
	custom_settings = {
		'FEED_URI' : 'tmp/reddit.csv'
	}

	def parse(self, response):
		#Extracting the content using css selectors(earlier logic)
		titles = response.css('.title.may-blank::text').extract()
		votes = response.css('.score.unvoted::text').extract()
		times = response.css('time::attr(title)').extract()
		comments = response.css('.comments::text').extract()
		#Give the extracted content row wise.
		for item in zip(titles,votes,times,comments):
			#create a dictionary of title, vote, publish date and comments
			scraped_info = {
				'title' : item[0],
				'vote' : item[1],
				'created_at' : item[2],
				'comments' : item[3],
			}
			#yield or give the scraped info to scrapy
			yield scraped_info
