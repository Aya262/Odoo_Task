from odoo import models,fields

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _inherit = ['mail.thread']

    name = fields.Char(string='Name',track_visibility='onchange')
    gender = fields.Selection([('female','Female'),('male','Male')],string='Gender' , default='male',track_visibility='onchange')
    country = fields.Char(string='Country',track_visibility='onchange')
    joining_date = fields.Date(string='Joining Date',track_visibility='onchange')
    tags = fields.Many2many('digizilla.tags',track_visibility='onchange')
    customers = fields.One2many('res.partner','digizilla',string='Customers',track_visibility='onchange')
    company = fields.Many2one('res.company',string='Company',track_visibility='onchange')
    notes = fields.Text(string='Notes',track_visibility='onchange')
    comments = fields.Char(string='Comments',track_visibility='onchange')
