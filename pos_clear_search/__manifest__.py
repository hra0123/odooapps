# -*- coding: utf-8 -*-

{
	'name':"POS Clear Search",
	'version':'14.1',
	'category':'Point of Sale',
	'summary':'POS Clear Search- clear the search items',
	'description':""" This module is used to clear items from search 
	""",
	'author':"Muhammed Aslam",
	'license': 'OPL-1',
	'website':'https://www.linkedin.com/in/muhammed-aslam-817327106/',
	'depends':['point_of_sale'],
	'data':[
		'views/assets.xml',
	],
	'images': ['static/description/banner.png'],
	'qweb': [
		'static/src/xml/clear_input_search.xml'
	],
	"auto_install": False,
	'installable': True,
}
