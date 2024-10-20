# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class AcademyGroup(models.Model):
    _name = "academy.group"
    _description = "academy.group"

    name = fields.Char(
        string="Academy group"
    )

    res_partner_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='academy_group_id',
        string='Students',
    )

    _sql_constraints = [
        ('name_unique', 'unique (name)', "The name of the group must be unique."),
    ]



