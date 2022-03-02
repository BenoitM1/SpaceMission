from odoo import models, fields


class Mission (models.Model):
    _name = 'mission.mission'

    name = fields.Char(string="Name")
    launch_date = fields.Datetime(string="Mission date de depart")
    return_date = fields.Datetime(string="Mission date d'arrivee")
    spaceship_id = fields.Many2one(comodel_name='spaceship', string="Vaisseau")
    crew_ids = fields.Many2many(comodel_name='res.partner', string="Equipage")
