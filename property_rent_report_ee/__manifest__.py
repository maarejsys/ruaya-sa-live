# See LICENSE file for full copyright and licensing details
{
    "name": "Property Rent Payment Voucher Report EE",
    "version": "13.0.1.0.0",
    'category': 'Real Estate',
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "website": "https://www.serpentcs.in/product/property-management-system",
    "summary": """
            Make report on payment receipt
            rent payment receipt
            rent receipt
            rent voucher
        """,
    'license': 'LGPL-3',
    'depends': ['property_management_ee', 'analytic', ],
    'data': [
        'views/report_property_rent_templates.xml',
        'views/report_configuration_view.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 19,
    'currency': 'EUR',
}
