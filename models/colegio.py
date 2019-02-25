from odoo import models,fields, api

class colegio(models.Model):
    _inherit = 'base.empresa'
    _name = 'colegio.colegio'
    name = fields.Char(string="nombre")
    direccion = fields.Char(string="direccion")
    clase_ids = fields.One2many("colegio.clase", "colegio_id", string="clases")
