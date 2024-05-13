from odoo import models,fields

class DigizillaTags(models.Model):
    _name = 'digizilla.tags'

    name=fields.Char(string='Name')