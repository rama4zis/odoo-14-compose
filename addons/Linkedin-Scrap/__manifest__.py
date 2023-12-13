# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Linkedin Scraping',
    'version': '1.0',
    'author'    : 'Rama',
    'category'   : 'Apps',
    'website' : 'http://github.com/rama4zis/',
    'description' : 'Linkedin Scraping Odoo Module',
    'depends': [
        # List Fitur
        'base',
    ],
    'data': [
        # List XML File Loaded 
        "menu.xml",

        # Views
        "views/company_scrap_view.xml",
        
        # Report
        # "report/work_order_report_view.xml",
        
        # Security
        "security/ir.model.access.csv",

       
    ],
}