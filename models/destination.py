from odoo import models, fields, api
class MissionDestination(models.Model):
    _name = 'mission.destination'

    name = fields.Char()
    code = fields.Char()