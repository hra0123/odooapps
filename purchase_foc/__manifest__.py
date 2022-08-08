# -*- coding: utf-8 -*-
{
    'name': 'Purchase Free of Cost Management',
    'version': '14.1',
    'category': 'Inventory',
    'sequence': 1,
    'summary': 'Manage free of cost in purchase order',
    'description': """
      This Odoo app help to manage free of cost in purchase order
      purchase free of cost management
      purchase foc 
      purchase
      purchase order foc
      purchase order free of cost
      foc
      free of cost
      free of cost management
      
    """,
    'author': 'Muhammed Aslam',
    'website': "https://www.linkedin.com/in/muhammed-aslam-817327106/",
    'depends': ['purchase'],
    'data': [
            'views/purchase_views.xml',
             ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
}