from odoo import models, fields, api
class MissionGradeandfonc(models.Model):
    _name = 'mission.gradeandfonc'

    namegra = fields.Char()
    codegra = fields.Char()
    namefonc = fields.Char()
    codefonc = fields.Char()