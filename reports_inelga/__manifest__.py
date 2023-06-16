# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": " Factura inelga",
    "summary": "Reports Inelga",
    "version": "14.0.0.1.0",
    "category": "Reports",
    "author": "SerinCloud, ",
    "website": "https://ingeniriacloud.com",
    "license": "AGPL-3",
    "depends": ['sales',

                ],
    "data": [
        "views/sale_order_report.xml",
        "views/external_inelga_layout_standard.xml",
    ],
    "installable": True,
}
