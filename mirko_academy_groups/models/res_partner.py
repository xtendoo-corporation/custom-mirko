# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Elegir entre los grupos creados en la tabla academy.group
    academy_group_id = fields.Many2one(
        comodel_name="academy.group",
        string="Academy group",
    )
