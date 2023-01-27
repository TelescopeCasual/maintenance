# Copyright 2019 Solvos Consultoría Informática (<http://www.solvos.es>)
# Copyright 2022 Telescope Casual Furniture
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Maintenance Project Plans",
    "summary": "Adds project and task to a Maintenance Plan",
    "version": "16.0.1.0.0",
    "author": "Odoo Community Association (OCA), Solvos, Telescope Casual Furniture",
    "license": "AGPL-3",
    "category": "Maintenance",
    "website": "https://github.com/telescopeCasual/maintenance",
    "depends": ["maintenance_plan", "maintenance_project"],
    "data": [
        "views/maintenance_equipment_views.xml",
        "views/maintenance_plan_views.xml",
    ],
    "demo": ["data/demo_maintenance_project_plan.xml"],
    "installable": True,
}
