from odoo import models
from asyncio.log import logger

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    def _create_invoices(self, sale_orders):
        invoive_ids = super(SaleAdvancePaymentInv, self)._create_invoices(sale_orders)
        
        index = 0
        for inv in invoive_ids:
            inv.po_spk_number_from_so = self.sale_order_ids[index].client_order_ref
            index += 1

        return invoive_ids