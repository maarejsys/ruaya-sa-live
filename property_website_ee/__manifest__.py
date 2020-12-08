# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details
{
    'name': 'Property Management Website EE',
    'description': 'This module will help you to manage your real estate portfolio with Property valuation, Maintenance, Insurance, Utilities and Rent management with reminders for each KPIs.',
    'category': 'Website',
    'version': '13.0.1.1.1',
    'license': 'LGPL-3',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'depends': ['base_geolocalize',
                'payment_paypal', 
                'property_ee',
                 'website'],
    'data': [
        'views/website_assets.xml',
        'views/assets_views.xml',
        'views/homepage_template.xml',
        'data/website_data.xml',
        'views/property_main_template.xml',
        'views/property_login_view.xml',
        'views/rent_properties_onload.xml',
        'views/selected_property_template.xml',
        'views/sell_property_template.xml',
        'views/my_property_template.xml',
        'views/website_property_filter.xml',
        'security/website_security.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png'],
    'application': True,
    'installable': True,
    'price' : 299,
    'currency': 'EUR',
}
