from odoo import models,fields, api

class estudiante(models.Model):
    _name = 'colegio.estudiante'
    name = fields.Char(string="nombre")
    apellidos = fields.Char(string="apellidos")
    notas = fields.Char(string="notas")
    clase_id = fields.Many2one("colegio.clase", string="clase")


