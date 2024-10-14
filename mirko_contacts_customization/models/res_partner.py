# Copyright (C) 2024 Manuel Calero (<https://xtendoo.es>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    type_contact = fields.Selection(
        selection=[
            ("others", "Others"),
            ("student", "Student"),
            ("teacher", "Teacher"),
        ],
        string="Contact type",
        default="others",
        required=True,
    )
    teacher_id = fields.Many2one(
        comodel_name="res.partner",
        string="Teacher"
    )

    def _get_contact_name(self, partner, name):
        return "%s, %s" % (name, partner.commercial_company_name or partner.sudo().parent_id.name)

