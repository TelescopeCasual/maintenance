# Copyright 2019 ForgeFlow S.L.
# Copyright 2022 Telescope Casual Furniture
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Base Maintenance",
    "version": "16.0.1.0.0",
    "author": "ForgeFlow, Odoo Community Association (OCA), Telescope Casual Furniture",
    "development_status": "Beta",
    "website": "https://github.com/telescopeCasual/maintenance",
    "category": "Maintenance",
    "license": "LGPL-3",
    "depends": ["maintenance"],
    "data": [
        "views/maintenance_team_views.xml",
        "views/maintenance_request_views.xml",
        "views/maintenance_equipment_views.xml",
        "views/report_maintenance_request.xml",
    ],
    "installable": True,
}
