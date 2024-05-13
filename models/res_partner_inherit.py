from odoo import  models,fields

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'


    digizilla = fields.Many2one('digizilla.digizilla')