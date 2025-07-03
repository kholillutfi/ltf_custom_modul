from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    po_spk_number_from_so = fields.Char('No Po/SPK')

