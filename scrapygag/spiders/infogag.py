# -*- coding: utf-8 -*-
import scrapy

class InfogagSpider(scrapy.Spider):
    name = 'infogag'
    allowed_domains = ['9gag.com/']
    start_urls = ['http://9gag.com/']

    def parse(self, response):
		titles = response.css(".badge-evt.badge-track::text").extract()
		votes = response.css(".point.badge-evt::text").extract()
		comments = response.css(".comment.badge-evt::text").extract()

		for item in zip(titles,votes,comments):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'comments' : item[2],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info