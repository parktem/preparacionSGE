from odoo import models,fields, api

class clase(models.Model):
    _name = 'colegio.clase'
    name = fields.Char(string="nombre")
    asignatura = fields.Char(string="asignatura")
    profesor = fields.Char(string="profesor")
    colegio_id = fields.Many2one("colegio.colegio", string="colegio")
    estudiante_ids = fields.One2many("colegio.estudiante", "clase_id", string="estudiantes")


    @api.one
    def generate_record_name(self):
        self.name = 'aleatorio'

