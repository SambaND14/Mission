# -*- coding: utf-8 -*-
# le fichier qui décrit le module
{
    'name' : 'Ordre de Mission',
    'summary': 'Ordre de mission',
    'sequense': 1,
    'description': """ Ce module est developpé par Samba Ndiaye""",
    'author' : 'Samba Ndiaye',
    'website': 'https://www.aibd.sn',
    'category': 'Services',
    'version' : '1.1',
    'depends' : ['base'],
    'data': [

        'views/employe.xml',
        'report/report.xml',
        'report/report_pdf.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
