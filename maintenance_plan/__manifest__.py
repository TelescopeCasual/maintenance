# Copyright 2017 Camptocamp SA
# Copyright 2022 Telescope Casual Furniture
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Maintenance Plan",
    "summary": "Extends preventive maintenance planning",
    "version": "16.0.1.0.0",
    "author": "Camptocamp SA, ForgeFlow, Odoo Community Association (OCA), Telescope Casual Furniture",
    "license": "AGPL-3",
    "category": "Maintenance",
    "website": "https://github.com/telescopeCasual/maintenance",
    "images": [],
    "depends": ["maintenance"],
    "data": [
        "security/ir.model.access.csv",
        "security/maintenance_security.xml",
        "views/maintenance_kind_views.xml",
        "views/maintenance_plan_views.xml",
        "views/maintenance_equipment_views.xml",
    ],
    "external_dependencies": {"python": ["python-dateutil"]},
    "demo": ["data/demo_maintenance_plan.xml"],
    "post_init_hook": "post_init_hook",
    "installable": True,
}
