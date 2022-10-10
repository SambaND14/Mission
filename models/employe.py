# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MissionEmploye(models.Model):
    _name = 'mission.employe'

    num = fields.Char("num", readonly=True, required=True, copy=False, default='New')
    name = fields.Char('Pénom et Nom')
    grade = fields.Char('Grade et fonction')
    dest = fields.Char('Se rendra à')
    motif = fields.Char('Motif de la mission')
    d_dep = fields.Date('Date de départ')
    d_rtr = fields.Date('Date de retour')
    transport = fields.Selection([('avion', 'Avion'), ('voiture', 'Voiture')])
    date = fields.Date('Dakar le,')


    @api.model
    def create(self, vals):
        if vals.get('num', 'New') == 'New':
            vals['num'] = self.env['ir.sequence'].next_by_code('mission.employe.sequence') or 'New'
        result = super(MissionEmploye, self).create(vals)
        return result


