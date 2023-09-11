from odoo import models, fields, api

class SaleOrderStatus(models.Model):
    _inherit = 'sale.order'

    invoice_status = fields.Selection([
        ('not_paid', 'No Pagado'),
        ('paid', 'Pagado'),
    ], string='Estado de Pago', compute='_compute_invoice_status', store=True)

    @api.depends('invoice_ids.state')
    def _compute_invoice_status(self):
        for order in self:
            unpaid_invoices = order.invoice_ids.filtered(lambda invoice: invoice.state == 'open')
            if unpaid_invoices:
                order.invoice_status = 'not_paid'
            else:
                order.invoice_status = 'paid'
