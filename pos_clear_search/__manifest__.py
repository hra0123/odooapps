# -*- coding: utf-8 -*-

{
	'name':"POS Clear Search",
	'version':'15.1',
	'category':'Point of Sale',
	'summary':'POS Clear Search- clear the search items',
	'description':""" This module is used to clear items from search 
	pos clear search
	pos reset search
	pos search
	pos clear search product
	pos advance search
	pos advance search clear
	pos exact search
	point of sale search
	point of sale clear search
	point of sale reset search
	point of sale advance search 
	point of sale exact search
	point of sale advance search clear
	point of sale clear search product 
	""",
	'author':"Muhammed Aslam",
	'website':'https://www.linkedin.com/in/muhammed-aslam-817327106/',
	'depends':['point_of_sale'],
	'data': [],
	'images': ['static/description/banner.jpg'],
	"auto_install": False,
	'installable': True,
	'assets': {
			'point_of_sale.assets': [
				'pos_clear_search/static/src/js/**/*',
			],
			'web.assets_qweb': [
				'pos_clear_search/static/src/xml/**/*',
			],
		},
}
