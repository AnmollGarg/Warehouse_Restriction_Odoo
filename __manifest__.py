{
    'name': 'Warehouse Restriction',
    'version': '1.0',
    'depends': ['base', 'stock', 'contacts', 'sale', 'account'],
    'data': [
        'security/warehouse_restriction_rules.xml',
        'views/res_users_view.xml',
    ],
    'installable': True,
    'application': True,
}