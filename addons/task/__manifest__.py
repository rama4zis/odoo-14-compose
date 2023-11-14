# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'task',
    'version': '1.0',
    'author'    : 'Rama',
    'category'   : 'Apps',
    'website' : 'http://github.com/rama4zis/',
    'description' : 'Task Odoo Module',
    'depends': [
        # List Fitur
        'base',
        'account',
        'sale'
    ],
    'data': [
        # List XML File Loaded 
        "menu.xml",

        # Views
        "views/work_order_view.xml",
        "views/service_team_view.xml",
        "views/sale_order_view.xml",
        
        # Report
        "report/work_order_report_view.xml",
        
        # Security
        "security/ir.model.access.csv",

       
    ],
}