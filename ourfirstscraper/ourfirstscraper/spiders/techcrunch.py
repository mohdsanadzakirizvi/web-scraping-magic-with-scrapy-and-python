# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpider(scrapy.Spider):
	#name of the spider
	name = 'techcrunch'
	#list of allowed domains
	allowed_domains = ['techcrunch.com/feed/']
	#starting url for scraping
	start_urls = ['http://techcrunch.com/feed/']
	#setting the location of the output csv file
	custom_settings = {
		'FEED_URI' : 'tmp/techcrunch.csv'
	}

	def parse(self, response):
		#remove xml namespaces
		response.selector.remove_namespaces()
		#extract info based on xpaths
		titles = response.xpath('//item/title/text()').extract()
		authors = response.xpath('//item/creator/text()').extract()
		dates = response.xpath('//item/pubDate/text()').extract()
		links = response.xpath('//item/link/text()').extract()

		for item in zip(titles, authors, dates, links):
			scraped_info = {
				'article_title' : item[0],
				'author' : item[1],
				'publish_date' : item[2],
				'article_link' : item[3],
			}
			yield scraped_info
